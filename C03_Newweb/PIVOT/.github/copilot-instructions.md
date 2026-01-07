# Copilot / AI agent instructions for PIVOT

목적: 이 저장소에 빠르게 생산적으로 기여하려는 AI 코딩 에이전트를 위한 실전 가이드입니다. 구체적 파일/패턴 예시와 실행 명령을 포함합니다.

1) 한눈에 아키텍처
- Frontend: React (Vite) 애플리케이션 — 소스는 `pivot_front/src/` (엔트리: `pivot_front/src/main.jsx`).
- Backend: FastAPI + SQLAlchemy — 엔트리: `pivot_back/main.py`. DB 연결은 `pivot_back/database.py`에서 구성.
- 데이터 흐름 예: 프론트엔드에서 회원가입 요청을 보내면 `/register` 엔드포인트(`pivot_back/main.py`)가 Pydantic 스키마(`pivot_back/schemas.py`)를 사용해 입력을 검증하고 SQLAlchemy 모델(`pivot_back/models.py`)로 DB에 저장합니다.

2) 개발/실행 요령 (재현 가능한 최소명령)
- 프론트엔드: 프로젝트 루트에서

  npm install
  cd pivot_front
  npm install
  npm run dev

  (프론트엔드는 Vite 기본 포트 `5173`에서 동작하며, CORS는 백엔드에서 `http://localhost:5173` 허용으로 설정되어 있음 — 확인: `pivot_back/main.py`)

- 백엔드: 환경변수(`.env`)에 DB 연결 정보를 넣어야 함 — 필수 키: `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_SERVICE` (참조: `pivot_back/database.py`).

  # 예시 (로컬 개발용)
  # .env 파일에 설정 후
  cd pivot_back
  python -m uvicorn main:app --reload --port 8000

  (프로젝트에 requirements.txt가 없으므로 FastAPI/uvicorn/sqlalchemy/python-dotenv/oracledb 등 필요한 패키지는 수동으로 설치해야 함.)

3) 프로젝트 관행 및 패턴
- React: 전역 사용자 상태는 `pivot_front/src/context/UserContext.jsx`의 `UserProvider`를 사용합니다. `App.jsx`는 `activeTab` 상태로 화면 전환을 제어합니다.
- 컴포넌트는 `pivot_front/src/components/`에 모여 있습니다(예: `Navbar.jsx`, `Dashboard.jsx`, `Login.jsx`, `Register.jsx`). 새로운 UI 컴포넌트는 이 구조를 따르세요.
- Backend: DB 세션은 `pivot_back/database.py`의 `get_db()` 의존성으로 주입됩니다. 엔드포인트는 Pydantic 스키마(`schemas.py`)를 요청/응답 형태로 사용합니다. 모델 정의는 `models.py`에서 확인하세요.
- DB 초기화: `models.Base.metadata.create_all(bind=database.engine)`가 `pivot_back/main.py`에서 호출되어 애플리케이션 시작 시 테이블을 생성합니다. 마이그레이션 도구는 현재 없음(수동 관리 필요).

4) 통합 포인트와 주의사항
- CORS: `pivot_back/main.py`에서 `allow_origins=["http://localhost:5173"]`로 고정되어 있습니다. 다른 dev 포트를 사용할 경우 변경 필요.
- Oracle: `pivot_back/database.py`는 Oracle 접속 문자열(`oracle+oracledb://...`)을 사용합니다. 로컬 개발 시 Oracle 드라이버와 DB 접근이 요구됩니다.
- 파일 업로드/바이너리: `models.User.profile_image`는 `LargeBinary`를 사용합니다 — 바이너리 저장/전송 방식에 유의하세요.

5) 코드 변경 시 권장 행동
- UI 변경: `pivot_front/src/components`에 컴포넌트 추가/수정 → 핫리로드로 빠르게 확인.
- API 변경: `schemas.py`와 `models.py`를 동시 업데이트. 스키마 필드를 바꾸면 관련 엔드포인트의 응답 모델 및 프론트 요청 페이로드를 함께 수정하세요.

6) 빠른 확인용 파일(예시)
- 프론트엔드 패키지: pivot_front/package.json
- 프론트 엔트리: pivot_front/src/main.jsx, pivot_front/src/App.jsx
- 전역 상태: pivot_front/src/context/UserContext.jsx
- 백엔드 엔트리: pivot_back/main.py
- DB 설정: pivot_back/database.py
- 모델: pivot_back/models.py
- 스키마: pivot_back/schemas.py

7) 무엇을 묻기 좋은가
- (환경) 이 저장소는 로컬 네트워크(LAN) 상의 다른 컴퓨터를 DB 서버로 사용합니다. 사용 중인 DB는 Oracle(`oracledb`)이며, 백엔드에 필요한 접속 정보(호스트/포트/서비스/사용자/비밀번호)는 이미 `pivot_back/database.py`에서 구성되도록 설계되어 있습니다. 에이전트가 작업할 때는 백엔드의 `pivot_back/database.py`와 로컬 `.env` 파일의 값을 참고하세요.
- (검증) 로컬에서 연결을 테스트하려면 `pivot_back`에서 환경변수 설정 후 `python -m uvicorn main:app --reload --port 8000`로 서버를 띄우고 프론트엔드 또는 curl로 `/register` 같은 엔드포인트를 호출해보세요.
- (권한) CI/CD 또는 도커 설정을 원하나요? 현재 관련 파일이 없습니다.

작업 완료 후 변경 사항을 커밋할 때 커밋 메시지는 간단명료하게 하세요(예: "feat: add register endpoint validation").

---
추가로 포함하길 원하는 예시나 규칙(예: 자주 쓰는 브랜치 이름, PR 템플릿)이 있으면 알려주세요. 불명확한 부분을 구체화해 반영하겠습니다.
