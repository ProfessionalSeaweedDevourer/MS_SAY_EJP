# Academy 리포 Phase 2 추가 지시 — 2026-04-20 Eric 검토 반영

본 지시는 `docs/session-reports/2026-04-20-academy-phase1-handoff.md`에 이어지는 Claude Code의 **Phase 2 시작 시점 추가 지시**다. handoff 문서의 `unresolved`·`next` 항목을 본 지시에 따라 실행한다. Claude Code는 다음 세션부터 이 순서대로 진행하되, 각 체크포인트에서 반드시 사용자 확인을 대기한다.

---

## 상위 원칙

1. Critical → Structure → Content 3단계 사이에 사용자 확인 체크포인트를 둔다. 한 세션에서 달리지 않는다.
2. **정직 우선**. 빈 섹션을 메우는 대신 "학습 중심, 영속 코드 없음"으로 남겨둔다. 특히 모듈 ④·PIVOT 저작 범위에서 준수.
3. 매 commit 전 `git diff --cached | grep -iE 'password|secret|key|token|bearer'` 자동 1회 실행하여 재유입 차단.

## Highlights 확정

이번 정비의 Highlights는 **2개**로 확정한다 (3개에서 축소).

1. **Azure AI Integration Suite** — `modules/06-azure-ai/`
2. **Seoul Air Quality MVC Pipeline** — `modules/01-foundations/1110_pyOOP_mvc_airquality/`

PIVOT은 Highlights에서 제외. 모듈 ③ README 본문에 "대표 실습 과제, 기술 테스트용 최소 규모"로 짧게만 언급. ML 진행 노트북·React Redux 다페이지 등 기타 후보는 모두 Highlights 탈락, 모듈 README 본문 언급으로만 한정.

---

## Phase 2 Critical 마무리

### Step 1 — 추가 시크릿 재스캔 (먼저)

- `ejp_lib/ejpDBManager.py`, `C01_python/1110_pyOOP_mvc_airquality/**/*.py`에서 DB 자격증명·하드코딩 엔드포인트 재검사
- `C03_Newweb/PIVOT/pivot_back/**` 전수 grep: `password=`, `SECRET`, `API_KEY`, `token`, 내부 IP 대역(`192.168.`, `10.`, `195.168.`)
- 전체 `*.ipynb` 셀 출력: 키·토큰·비밀번호 에코 여부
- 발견 시 Phase 1 패턴(os.environ 전환) 적용, 필요 시 `git-filter-repo --replace-text` 추가 실행

### Step 2 — Working tree 정리 단일 commit

**삭제 대상** (`git rm -r`):

- `node_modules/` 55세트, `__pycache__/` 34곳
- `workspace6/`, `.vscode/` (선택, `settings.json`만)
- `leeKNNModel/model.pkl` (재현 가능성 미확보)
- 루트 `subway.csv` (86MB), `lnps.csv` (55MB) — 출처 링크만 README에 유지
- Windows `.lnk` 바로가기 2개, `C01_python/1113_nothing/`
- `hangul-utils-master/` — 서드파티 벤더링 취소, README에 원본 링크만 유지
- **`MS_AISA 18/`** — 사용자 판단: MS_AISA 전 세트가 레퍼런스용, Eric 산출물 아님 → 전체 제거
- 사용자가 로컬 삭제한 247건 working tree 반영분 (`교재/`, `25-3-super-compressed_v1-2.pdf`, `misc/` 시험 PDF, MS_AISA 12~17)

**신규 작성**:

- `.gitignore`: `__pycache__/`, `*.pyc`, `.ipynb_checkpoints/`, `.env`, `.env.*`, `!.env.example`, `venv/`, `.venv/`, `node_modules/`, `.vscode/`, `.DS_Store`, `workspace6/`, `*.pkl`
- `.env.example`: 구 `.env` 2건에서 확인된 변수명만 플레이스홀더로 복원. 실제 값 금지.

**commit 메시지**: `chore: clean build artifacts, IDE files, vendored third-party, and reference team projects`

### Step 3 — 체크포인트 A

Critical 커밋 push 후 세션 중단. 사용자 확인 후 다음 세션에서 Structure 진입.

---

## Phase 2 Structure

### Step 4 — 모듈 디렉토리 재배치 (`git mv`로 history 보존)

배치:

- `modules/01-foundations/` ← `C01_python/` 대부분 (기초·OOP·DB·크롤링·NumPy·Pandas·Jan26_ML)
- `modules/02-data-ingestion/` ← `C01_python/1103_pyWebcrawl/`, `C02_web/1118_css_and_pyWebcrawl/`, `C02_web/1201_Webparse_ExternalAPI/`, `C02_web/1202_KakaomapAPI_*/`
- `modules/03-fullstack/` ← `C02_web/*` (Flask/FastAPI/Node), `C03_Newweb/dec10~dec24/*`, `C03_Newweb/PIVOT/`
- `modules/04-azure-infra/` ← 빈 디렉토리. README만 Content 단계에서 생성.
- `modules/05-ai-theory/` ← `C04_AI/Jan27_base/`, `Jan29_tf/`, `Jan30_tf/`
- `modules/06-azure-ai/` ← `C04_AI/Feb03_AzureAI/`, `Feb04_azureAI/`, `Feb05_Azure_Language/`

추가 사항:

- `Setup/`, `ejp_lib/`, `templates/`는 루트 유지. 이동 판단 사용자 확인.
- 경로 참조(python import·노트북) 작동 재검증은 하지 않음 — "학습 스냅샷" 포지셔닝으로 우선순위 낮음.

### Step 5 — 체크포인트 B: 사용자 직접 작성 블록 배치

다음 파일에 Claude Code가 TODO 마커만 생성:

- `modules/03-fullstack/PIVOT/README.md`
- `modules/01-foundations/1110_pyOOP_mvc_airquality/README.md`
- `modules/06-azure-ai/README.md`

TODO 마커 템플릿(세 파일 모두 동일):

    ## 저작 범위 <!-- TODO: Eric 직접 작성. 수업 제공 / 본인 구현 / (팀 프로젝트인 경우) 팀 기여 3항목으로 분리 -->

    - **수업 제공**: [ ]
    - **본인 구현**: [ ]
    - **(해당 시) 팀 기여**: [ ]

Eric이 3개 블록 모두 채우기 전까지 Content 단계로 진행하지 않는다.

---

## Phase 2 Content

### Step 6 — 루트 `README.md` (KO + EN 병기, 직역 금지)

**KO 섹션 구성**:

- 상단: Microsoft × 성균관대 K-Digital Training, 2025.10–2026.04, 약 800시간
- 수료 증빙 블록: AI-900 자격증 이미지 + 수료증 이미지 (`assets/` 배치)
- 6개 모듈 맵 (테이블)
- Highlights 섹션: 2개(Azure AI Integration Suite · Seoul Air Quality MVC Pipeline)만. 각 1~2문장 + 모듈 경로 링크.
- 관련 프로젝트: SOHOBI 링크 + "Academy에서 학습한 기술이 SOHOBI 팀 프로젝트의 기반이 됨" 한 줄
- MIT 라이선스 표기

**EN 섹션 (별도 재작성, 직역 아님)**:

    # Coursework archive — MS AI SW Academy

    K-Digital Training program co-run by Microsoft Korea and SKKU,
    Oct 2025 – Apr 2026. 6 modules, ~800 hours. Azure AI-900 obtained
    during the program. This repo archives deliverables per module;
    original team projects (e.g., SOHOBI) live in separate repositories:
    https://github.com/ProfessionalSeaweedDevourer/SOHOBI

이하 모듈 맵·Highlights·라이선스 KO와 동일 구조.

### Step 7 — 모듈 ④ README (B안 + C안 혼합)

파일: `modules/04-azure-infra/README.md`

본문:

    # Module 4 — Azure Infrastructure

    **기간**: 2026.01 (추정)
    **핵심 개념**: Azure VM, Linux 원격 접속, 클라우드 컴퓨팅 기초, Azure Portal·CLI

    ## 학습 범위
    - Azure VM 생성·관리, Linux 기본 명령·SSH 원격 접속
    - 클라우드 컴퓨팅 개념(IaaS/PaaS/SaaS), 리전·가용영역
    - Azure Cloud 인프라 구축 실습, 개발 환경 설정·배포

    ## 산출물
    본 모듈은 Azure Portal·CLI 중심 실습으로 진행되어 영속 코드 산출물이 없다.
    실질적 적용 결과는 팀 프로젝트 SOHOBI의 프로덕션 인프라에서 확인 가능하다:

    - Azure Static Web App (Frontend)
    - Azure Container Apps (Backend, Dockerfile 기반 CI/CD)
    - Azure PostgreSQL Flexible Server
    - Cosmos DB (PostgreSQL API)
    - Azure AI Search + 자체 search index
    - Azure Blob Storage (로그 영구 저장, 관리형 아이덴티티)

    → SOHOBI 리포: https://github.com/ProfessionalSeaweedDevourer/SOHOBI

영문판은 동일 구조 재작성.

### Step 8 — 나머지 5개 모듈 README

지시문 원본 템플릿 사용. **공백 채우기 금지**. 산출물이 없는 항목은 "수업 중 실습, 영속 파일 없음" 또는 "개인 노트로 별도 보관"으로 명시.

### Step 9 — `LICENSE` (MIT), 필요 시 `.nojekyll`

### Step 10 — 노트북 output 선별 정리

키·토큰·개인정보·대용량 덤프만 제거. 학습 흔적 보존.

### Step 11 — 체크포인트 C

영문판 별도 검수 + Highlights 2개 내용 확인 + 저작 범위 블록 완료 여부 확인.

---

## Phase 3 Highlights 심화 (별도 세션)

### 1. Azure AI Integration Suite — `modules/06-azure-ai/README.md` 심화

- 8개 Azure Cognitive Services 사용 흐름
- 각 서비스별 입력·출력 예시 (키 제거된 실행 결과)
- AI-900 자격증 서사 연결

### 2. Seoul Air Quality MVC Pipeline — `modules/01-foundations/1110_pyOOP_mvc_airquality/README.md` 심화

- 공공 API → XML 파싱 → Oracle 저장 → CSV 산출 파이프라인 다이어그램
- OOP/MVC 분리 근거 한 단락
- 재현 가이드 (`.env.example` 참조)

---

## 절대 금지 (재강조)

- `.env`·key·토큰 history 재유입
- 모듈 ④ README에 실제 구현 안 한 내용 기재
- MS_AISA 디렉토리 부활
- 서드파티 라이브러리 재벤더링
- 저작 범위 블록 TODO 상태에서 Content 단계 진입

---

## 공개 전환 전 최종 체크 (사용자 수동)

> **NOTE (2026-04-20)**: Azure 계정이 교육과정 종료로 잠김 → rotate 불가능·불필요. history redact(filter-repo)가 유일한 시크릿 대응이며 Step 2에서 완료.

- [x] Azure 키 rotate — 계정 잠금으로 N/A
- [ ] `git log --all --source -S "***REDACTED"` 로 redact 흔적만 남았는지 확인
- [ ] 저작 범위 블록 3개 Eric 작성 완료
- [ ] 영문 README 별도 검수 완료
- [ ] `gh repo edit --visibility public` — Claude Code 실행 금지, Eric 직접

---

**지시 종료. 다음 세션은 Step 1 (추가 시크릿 재스캔)부터 시작.**
