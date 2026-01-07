**Purpose**
- **Goal:** 빠르게 이 리포지토리에서 생산적으로 코드를 작성·수정할 수 있도록 AI 코딩 에이전트에게 필요한 핵심 정보만 제공.

**프로젝트 개요**
- **프레임워크:** FastAPI 애플리케이션 (`main.py`) — 단일 모듈로 HTTP 엔드포인트를 노출합니다.
- **영속성:** SQLAlchemy ORM 사용, 데이터베이스는 Oracle (oracledb) 연결 (`database.py`).
- **주요 모델:** `models.py`에 `User` 테이블 정의 (필드: `id`, `password`, `birth_date`, `address`, `profile_image`).

**핵심 흐름 (예시)**
- 가입 엔드포인트: `POST /register` (`main.py`) — `schemas.UserCreate`를 받아 `models.User`로 저장.
- DB 세션: `database.get_db()` 의존성으로 세션을 생성/종료함.
- DB 초기화: 앱 시작 시 `models.Base.metadata.create_all(bind=database.engine)` 호출 (마이그레이션 없음).

**환경 및 실행**
- 필수 환경변수: `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_SERVICE` (`.env`로 관리, `python-dotenv` 사용).
- 로컬 실행 (예시, PowerShell):

```powershell
# .env에 값 설정 후
pip install -r requirements.txt  # 없으면 fastapi, uvicorn, sqlalchemy, python-dotenv 등 설치
uvicorn main:app --reload --port 8000
```

**프로젝트 특이사항 / 규칙**
- CORS는 프런트(React dev server `http://localhost:5173`)에만 열려 있음 (`main.py`의 `CORSMiddleware`).
- DB URL은 `database.py`에서 Oracle 전용 형식으로 구성됨 — 변경 시 Oracle 용 드라이버 옵션을 확인하세요.
- 스키마/응답: `schemas.py`의 Pydantic 모델을 통해 요청/응답을 명시함 (`UserCreate`, `UserResponse`).
- Pydantic 설정: 프로젝트에서 `UserResponse`에 `Config.from_attributes = True`가 사용되어 있음 — 값 직렬화 방법을 변경할 때 주의.

**개발자/AI 에이전트 지침 (구체적)**
- 변경 전: 모델 필드 추가/수정은 DB 스키마 변경을 의미하니, 수동 마이그레이션 또는 데이터 덤프·복구 전략을 제안하세요.
- 새로운 엔드포인트 추가 시: `schemas`에 요청·응답 모델을 추가하고, `main.py`에 의존성으로 `db: Session = Depends(database.get_db)`를 사용하세요.
- 비밀번호 처리: 현재 평문 저장 코드가 있으니(발견됨) — 보안 수정을 제안할 때는 `passlib` 등 해시 적용을 권장하세요.
- 바이너리(프로필 이미지): `LargeBinary` 사용 — 대용량 파일 업로드 설계 변경 시 파일 스토리지(S3 등) 권장.

**참고 파일 (빠른 링크)**
- `main.py` — HTTP 엔드포인트와 CORS 설정
- `database.py` — DB 연결 및 세션 생성/종료 패턴
- `models.py` — SQLAlchemy 모델 정의 (User)
- `schemas.py` — Pydantic 요청/응답 모델

**제한된 추론 / 금지 행동**
- 직접 비밀(환경변수 값)을 코드에 하드코딩하지 마십시오.
- 마이그레이션 없이 스키마를 임의로 변경하여 데이터 손실을 발생시키지 마십시오.

피드백: 이 파일 내용에서 더 추가하거나 분명히 했으면 하는 부분을 알려주세요.
