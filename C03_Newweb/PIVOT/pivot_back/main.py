from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Request
from fastapi.responses import Response
import os
from pathlib import Path
# JWT removed — using signed-cookie sessions instead
import logging
from datetime import timedelta
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.orm import Session
import models, schemas, database
import uuid
from datetime import datetime

# Session / secret settings
SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret_change_me')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', '60'))

app = FastAPI()

logger = logging.getLogger("uvicorn.error")

# React 접속 허용 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type", "Accept", "Origin", "User-Agent"],
)

# Signed cookie session middleware (server signs cookie; session stored client-side but tamper-proof)
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY, session_cookie='session', max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60, same_site='lax')

# 테이블 생성 (최초 실행 시)
models.Base.metadata.create_all(bind=database.engine)

# storage settings
BASE_DIR = Path(__file__).resolve().parent
PROFILE_IMG_DIR = BASE_DIR / 'static' / 'profile_images'
PROFILE_IMG_DIR.mkdir(parents=True, exist_ok=True)
MAX_UPLOAD_BYTES = 5 * 1024 * 1024  # 5 MB
ALLOWED_MIMES = {
    'image/png': 'png',
    'image/jpeg': 'jpg',
    'image/jpg': 'jpg',
    'image/gif': 'gif',
    'image/webp': 'webp',
}


def get_current_user(request: Request, db: Session = Depends(database.get_db)) -> models.User:
    """Return user from server-side session (signed cookie)."""
    user_id = None
    try:
        user_id = request.session.get('user_id')
    except Exception:
        user_id = None

    logger.info(f"get_current_user: session_user_id={user_id}")

    if not user_id:
        raise HTTPException(status_code=401, detail='로그인 세션이 없습니다.')

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='사용자를 찾을 수 없습니다.')
    return user

@app.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # ID 중복 체크
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    if db_user:
        raise HTTPException(status_code=400, detail="이미 등록된 아이디입니다.")
    
    # 신규 유저 저장
    new_user = models.User(
        id=user.id,
        password=user.password,
        birth_date=user.birth_date,
        address=user.address
    )
    
    db.add(new_user)
    db.commit()
    return {"id": new_user.id, "message": "회원가입 성공"}


@app.post("/login", response_model=schemas.LoginResponse)
def login_user(user: schemas.UserLogin, request: Request, db: Session = Depends(database.get_db)):
    # 사용자 조회
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="아이디 또는 비밀번호가 일치하지 않습니다.")

    # 로그인 성공: 세션에 사용자 id 저장 (서명된 쿠키로 클라이언트에 전달)
    request.session['user_id'] = db_user.id

    # 응답: 간단한 사용자 정보 (토큰 대신 세션 사용)
    return {
        "id": db_user.id,
        "name": db_user.id,
        "birth_date": db_user.birth_date,
        "address": db_user.address,
    }


@app.post("/users/{user_id}/profile-image")
async def upload_profile_image(user_id: str, file: UploadFile = File(...), request: Request = None, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    # current_user comes from get_current_user dependency and is already validated
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail='자신의 프로필만 변경할 수 있습니다.')

    db_user = current_user
    # 디버그: 요청 헤더 키 목록 및 Authorization 존재 여부 로깅
    try:
        header_keys = list(request.headers.keys()) if request is not None else []
        auth_present = any(k.lower() == 'authorization' for k in header_keys)
    except Exception:
        header_keys = None
        auth_present = False
    logger.info(f"upload_profile_image: called for user={user_id} current_user={current_user.id} auth_present={auth_present} headers={header_keys}")

    # basic MIME/type validation
    content_type = (file.content_type or '').lower()
    if content_type not in ALLOWED_MIMES:
        raise HTTPException(status_code=400, detail="허용되지 않는 이미지 형식입니다.")

    content = await file.read()
    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=400, detail="파일 크기가 허용 한도(5MB)를 초과했습니다.")

    ext = ALLOWED_MIMES[content_type]
    filename = f"{user_id}.{ext}"
    filepath = PROFILE_IMG_DIR / filename

    # write file to disk
    with open(filepath, 'wb') as f:
        f.write(content)

    # update db with filename and mime
    db_user.profile_image_filename = str(filename)
    db_user.profile_image_mime = content_type
    db.add(db_user)
    db.commit()

    return {"url": f"/users/{user_id}/profile-image"}


@app.get("/users/{user_id}/profile-image")
def get_profile_image(user_id: str, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
    if not db_user.profile_image_filename:
        raise HTTPException(status_code=404, detail="프로필 이미지가 없습니다.")

    filepath = PROFILE_IMG_DIR / db_user.profile_image_filename
    if not filepath.exists():
        raise HTTPException(status_code=404, detail="프로필 이미지 파일을 찾을 수 없습니다.")

    with open(filepath, 'rb') as f:
        content = f.read()

    mime = db_user.profile_image_mime or 'application/octet-stream'
    return Response(content=content, media_type=mime)


@app.post('/posts', response_model=schemas.PostResponse)
def create_post(payload: schemas.PostCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    author_id = current_user.id
    db_user = current_user

    post_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()
    post = models.Post(id=post_id, author_id=author_id, content=payload.content, created_at=now)
    db.add(post)
    # increment user's post_count
    try:
        db_user.post_count = (db_user.post_count or 0) + 1
    except Exception:
        db_user.post_count = 1
    db.add(db_user)
    db.commit()
    return {
        'id': post_id,
        'author_id': author_id,
        'content': payload.content,
        'created_at': now,
        'comments': []
    }


@app.delete('/posts/{post_id}')
def delete_post(post_id: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail='게시글을 찾을 수 없습니다.')
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail='자신의 게시글만 삭제할 수 있습니다.')

    # decrement post_count for author
    try:
        current_user.post_count = max(0, (current_user.post_count or 0) - 1)
    except Exception:
        current_user.post_count = 0

    # find comments for this post and decrement comment_count for each comment author
    comments = db.query(models.Comment).filter(models.Comment.post_id == post_id).all()
    for c in comments:
        author = db.query(models.User).filter(models.User.id == c.author_id).first()
        if author:
            try:
                author.comment_count = max(0, (author.comment_count or 0) - 1)
            except Exception:
                author.comment_count = 0
            db.add(author)
        db.delete(c)

    db.add(current_user)
    db.delete(post)
    db.commit()
    return {'detail': 'deleted'}


@app.get('/posts')
def list_posts(request: Request, db: Session = Depends(database.get_db)):
    posts = db.query(models.Post).order_by(models.Post.created_at.desc()).all()
    result = []
    for p in posts:
        comments = db.query(models.Comment).filter(models.Comment.post_id == p.id).all()
        comment_list = []
        for c in comments:
            # try to get author's name
            c_user = db.query(models.User).filter(models.User.id == c.author_id).first()
            comment_list.append({
                'id': c.id,
                'post_id': c.post_id,
                'author_id': c.author_id,
                'author_name': c_user.name or c_user.id if c_user else c.author_id,
                'author_profile': (f"{str(request.base_url).rstrip('/')}/users/{c.author_id}/profile-image" if c_user and c_user.profile_image_filename else ''),
                'content': c.content,
                'created_at': c.created_at
            })

        p_user = db.query(models.User).filter(models.User.id == p.author_id).first()
        result.append({
            'id': p.id,
            'author_id': p.author_id,
            'author_name': p_user.name or p_user.id if p_user else p.author_id,
            'author_profile': (f"{str(request.base_url).rstrip('/')}/users/{p.author_id}/profile-image" if p_user and p_user.profile_image_filename else ''),
            'content': p.content,
            'created_at': p.created_at,
            'comments': comment_list
        })
    return result


@app.post('/posts/{post_id}/comments')
def add_comment(post_id: str, payload: schemas.CommentCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    author_id = current_user.id
    db_user = current_user
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail='게시글을 찾을 수 없습니다.')

    comment_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()
    comment = models.Comment(id=comment_id, post_id=post_id, author_id=author_id, content=payload.content, created_at=now)
    db.add(comment)
    try:
        db_user.comment_count = (db_user.comment_count or 0) + 1
    except Exception:
        db_user.comment_count = 1
    db.add(db_user)
    db.commit()
    return {'id': comment_id, 'post_id': post_id, 'author_id': author_id, 'content': payload.content, 'created_at': now}


@app.delete('/posts/{post_id}/comments/{comment_id}')
def delete_comment(post_id: str, comment_id: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id, models.Comment.post_id == post_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail='댓글을 찾을 수 없습니다.')
    if comment.author_id != current_user.id:
        raise HTTPException(status_code=403, detail='자신의 댓글만 삭제할 수 있습니다.')

    try:
        current_user.comment_count = max(0, (current_user.comment_count or 0) - 1)
    except Exception:
        current_user.comment_count = 0

    db.delete(comment)
    db.add(current_user)
    db.commit()
    return {'detail': 'deleted'}


@app.get("/users/{user_id}", response_model=schemas.LoginResponse)
def get_user(request: Request, user_id: str, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

    profile_url = None
    if db_user.profile_image_filename:
        profile_url = f"{str(request.base_url).rstrip('/')}/users/{db_user.id}/profile-image"

    return {
        "id": db_user.id,
        "name": db_user.name or db_user.id,
        "birth_date": db_user.birth_date,
        "address": db_user.address,
        "role": db_user.role,
        "description": db_user.description,
        "profile_image_url": profile_url,
        "post_count": db_user.post_count or 0,
        "comment_count": db_user.comment_count or 0,
    }


@app.put("/users/{user_id}", response_model=schemas.LoginResponse)
def update_user(request: Request, user_id: str, payload: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

    # Update allowed fields
    if payload.name is not None:
        db_user.name = payload.name
    if payload.role is not None:
        db_user.role = payload.role
    if payload.description is not None:
        db_user.description = payload.description

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    profile_url = None
    if db_user.profile_image_filename:
        profile_url = f"{str(request.base_url).rstrip('/')}/users/{db_user.id}/profile-image"

    return {
        "id": db_user.id,
        "name": db_user.name or db_user.id,
        "birth_date": db_user.birth_date,
        "address": db_user.address,
        "role": db_user.role,
        "description": db_user.description,
        "profile_image_url": profile_url,
        "post_count": db_user.post_count or 0,
        "comment_count": db_user.comment_count or 0,
    }