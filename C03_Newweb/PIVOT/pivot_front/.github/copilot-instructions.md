# Copilot / AI agent instructions for PIVOT (pivot_front)

짧고 구체적인 지침: 이 저장소는 React + Vite 기반의 프론트엔드(클라이언트)입니다. 에이전트는 아래 핵심 항목에 집중해 작업하세요.

**아키텍처 개요**
- **프론트엔드:** React 19 + Vite (entry: [src/main.jsx](src/main.jsx#L1))
- **스타일:** TailwindCSS 플러그인 사용 (설정: [vite.config.js](vite.config.js#L1))
- **상태/컨텍스트:** 전역 유저 상태는 [src/context/UserContext.jsx](src/context/UserContext.jsx#L1)에서 제공. `userInfo`와 `setUserInfo`를 통해 컴포넌트 간 데이터 공유.
- **컴포넌트:** 주요 뷰는 [src/components](src/components) 내부. `App.jsx`가 탭 기반 렌더링과 라우트 역할을 단순히 수행함: [src/App.jsx](src/App.jsx#L1)

**핵심 워크플로우 / 커맨드**
- 개발 서버: `npm run dev` (Vite HMR)
- 빌드: `npm run build`
- 미리보기: `npm run preview`
- 린트: `npm run lint` (ESLint 설정이 포함되어 있음)

**프로젝트 규약 / 패턴**
- 컴포넌트 위치: 모든 UI는 `src/components/*`에 위치합니다.
- 전역 데이터는 반드시 `UserContext`를 통해 전달합니다. 예: `Dashboard`와 `Register`는 `UserContext`를 사용합니다.
- 스타일은 Tailwind 유틸리티 클래스를 선호합니다(인라인 className 사용).
- 탭 전환은 `App.jsx`의 `activeTab` 상태로 제어됩니다 — 새로운 화면을 추가할 때 이 패턴을 따르세요.

**통합 포인트 / 외부 의존성**
- 백엔드: 프론트는 로컬 FastAPI 서버(예: `http://localhost:8000`)와 통신하도록 작성되어 있습니다. 예: [src/components/Register.jsx](src/components/Register.jsx#L1) 내의 `fetch('http://localhost:8000/register')` 호출.
- 데이터베이스: 컴포넌트 주석에 Oracle DB 연동 언급이 있으나 실제 DB 코드는 백엔드(FastAPI)에서 처리됩니다. 프론트는 JSON API 계약을 준수해야 함.

**코드 예시(패턴 참조)**
- 사용자 등록: [src/components/Register.jsx](src/components/Register.jsx#L1-L120) — 폼 상태를 로컬로 관리한 뒤 `fetch`로 POST, 성공 시 `setUserInfo(formData)` 호출.
- 프로필 표시: [src/components/Dashboard.jsx](src/components/Dashboard.jsx#L1-L40) — `userInfo`의 존재 여부에 따라 기본값(`||`)을 사용.

**에이전트 행동 규칙 (구체적)**
- 변경사항을 만들 때는 최소 침범 원칙을 따르세요 — 파일 구조 및 기존 컴포넌트 패턴을 따르며 Tailwind 클래스를 사용하세요.
- 네트워크 엔드포인트(예: `http://localhost:8000`)를 변경하거나 하드코딩할 때는 PR/코멘트로 이유를 남기세요.
- 새 API 호출을 추가할 때 응답 실패(HTTP 비-OK) 처리와 네트워크 예외 처리를 반드시 포함하세요(현재 `Register.jsx` 패턴 참고).
- ESLint 규칙을 유지하세요 (`npm run lint`로 검사). 코드 스타일은 기존 파일을 따르세요.

**참고 파일 (빠른 링크)**
- 시작점: [src/main.jsx](src/main.jsx#L1)
- 앱 레이아웃: [src/App.jsx](src/App.jsx#L1)
- 유저 컨텍스트: [src/context/UserContext.jsx](src/context/UserContext.jsx#L1)
- 회원가입 예시: [src/components/Register.jsx](src/components/Register.jsx#L1)

피드백: 이 파일을 검토한 뒤, 누락된 통합 포인트나 더 상세히 문서화할 항목을 알려주세요.
