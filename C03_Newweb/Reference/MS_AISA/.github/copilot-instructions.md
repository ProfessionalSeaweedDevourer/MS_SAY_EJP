## 프로젝트 개요

- **기술 스택**: React (v19) + Vite, Redux Toolkit, axios. 빌드/개발: `npm run dev` (Vite).
- **구조 요약**: UI는 `src/msAISA` 아래에서 구성됩니다. 레이아웃 컴포넌트는 `msAISAMain.jsx`가 루트 역할을 하며 `Title`, `Content`, `Menu`, `Weather` 컴포넌트를 렌더합니다.

## 주요 아키텍처 포인트

- 라우팅: `src/App.jsx`에서 `Routes`를 정의. `MSAISAMain`이 레이아웃 래퍼로 사용됩니다.
- 전역 상태: Redux store는 `src/main.jsx`에서 설정되며, 슬라이스는 `src/slice`에 있음 (`memberSlice.js`, `loginSystemSummonSlice.js`). 슬라이스 이름은 `ms`(회원 관련)와 `lsss`(로그인 창 소환)입니다.
- 인증/세션: `src/msAISA/msAISAMain.jsx`의 `loginCheck` 함수가 `sessionStorage`와 `http://localhost:9999`의 REST 엔드포인트를 사용하여 로그인 상태를 확인하고 갱신합니다. UI가 전역 이벤트 리스너(`document.addEventListener('click', loginCheck)`)에 의존하므로 변경 시 주의하세요.

## 개발/디버깅 워크플로우

- 실행: `npm run dev` (Vite 개발 서버, HMR). 빌드: `npm run build`. 미리보기: `npm run preview`.
- 린트: `npm run lint` (프로젝트 루트에 ESLint 설정 존재).
- 백엔드 연동: 로컬 API 호출은 `http://localhost:9999`를 사용합니다—통합 개발 시 동일 호스트/포트로 백엔드를 실행하거나 프록시 설정 필요.

## 코드베이스 패턴 & 컨벤션 (프로젝트 고유)

- CSS는 각 컴포넌트에서 상대 경로로 직접 import 합니다. 예: `src/msAISA/msAISAMain.jsx`에서 여러 CSS import.
- 슬라이스 상태 변경은 `createSlice`의 리듀서로 직접 변경(immer 적용)합니다. 예: `memberSlice.js`의 `setLoginMember`.
- UI 토글 상태(로그인창)는 숫자 좌표(`bottom`)와 `opacity` 값으로 제어됩니다 — 스타일 기반 애니메이션 기대.
- 라우트 경로 규칙: 페이지 이동 경로가 파일명과 1:1 맵핑되지 않음 (`/sign.up.go` → `signUpForm.jsx`). 라우트 문자열을 변경할 때는 `App.jsx`와 링크들을 함께 업데이트하세요.

## 안전/주의사항

- `msAISAMain.jsx`가 전역 `document` 클릭 리스너를 등록하여 `loginCheck`를 호출합니다. 이 로직을 수정하면 전역 동작에 영향을 줍니다.
- `loginCheck`는 네트워크 응답에 따라 `sessionStorage`와 네비게이션(`useNavigate`)을 조작합니다. 비동기 실패 케이스(에러 핸들링)가 제한적이므로 네트워크 오류 시 사용자 경험 문제가 발생할 수 있습니다.

## 빠른 레퍼런스 (예시 파일)

- 레이아웃 엔트리: src/msAISA/msAISAMain.jsx
- 라우팅: src/App.jsx
- 스토어 설정: src/main.jsx
- 회원 슬라이스: src/slice/memberSlice.js
- 로그인 모달 슬라이스: src/slice/loginSystemSummonSlice.js

## 작업 지침(에이전트에게)

- 변경 범위를 좁게 가져가세요: 레이아웃/글로벌 상태를 수정할 때는 `msAISAMain.jsx`, `main.jsx`, `App.jsx`를 함께 확인하세요.
- API 경로(`http://localhost:9999`)를 하드코딩해 변경할 경우, 해당 호출을 모두 찾아 일관되게 업데이트하세요.
- UI 토글/애니메이션은 슬라이스에서 수치 값을 직접 변경하는 방식이므로 CSS와 함께 동작을 확인하세요.

---
생성/병합이 완료되었습니다. 불명확하거나 더 상세히 문서화할 부분을 알려주시면 수정하겠습니다.
