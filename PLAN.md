# PLAN.md — Academy 리포 공개 정비 Phase 1 실태 조사 보고서

작성일: 2026-04-20
작성자: Claude Code (Phase 1 · 실태 조사)
지시문: [Instructions/INSTRUCTIONS.md](Instructions/INSTRUCTIONS.md)

> 이 문서는 `Instructions/INSTRUCTIONS.md`가 규정한 **Phase 1(실태 조사)** 산출물이다. 본 세션에서 파일 이동·삭제·수정은 수행하지 않았다. Phase 2는 문서 말미 **필수 질문**에 대한 사용자 응답 후 별도 세션에서 진행한다.

---

## 1. 디렉토리 트리 (3 depth)

`.git`, `node_modules`, `__pycache__`, `.ipynb_checkpoints`, `venv` 등 런타임 아티팩트 제외.

```
MS_SAY_EJP/
├── C01_python/                     # 30 subdirs (Oct–Feb)
│   ├── 1015_VSCode, 1016_pyVar, 1017_pyIO_calc
│   ├── 1020_pyLogic_collection ~ 1031_pyOOP_loop
│   ├── 1103_pyWebcrawl, 1107_pyDBconn_fromnov03
│   ├── 1110_pyOOP_mvc_airquality/{ejp}
│   ├── 1111_pyMVC_prac_webmall/{MWM, Nov11_1_Python}
│   ├── 1112_pyMVC_expense/{MyExpense}
│   ├── 1113_nothing, 1114_pyMongoDB
│   ├── Jan14_numpy, Jan16_pd, Jan19_pd
│   ├── Jan20/{1_pd, 2_matplotlib}, Jan21
│   ├── Jan22_Backup, Jan23_Backup/{1_Text, 2_Image}
│   └── Jan26_ML
├── C02_web/                        # 21 subdirs (Nov–Dec)
│   ├── 1117_htmlbasics/{testimage}
│   ├── 1118_css_and_pyWebcrawl/{Crawling, Mobile}
│   ├── 1119_pyWeb_FastAPI_Reg/{IO, web(1119)}
│   ├── 1120_pyWeb_FastAPI_FileUpload/{js}
│   ├── 1124_JSbasics/{JS}
│   ├── 1125_JS_BMIcalc/{BMITEST, NewWeb, NewWeb_Backend}
│   ├── 1126_JS_JQuery_basic
│   ├── 1127_JS_Event_HTML5_Canvas/{HTML5_canvas}
│   ├── 1128_HTML5_game_JQ_webparse/{h5_can, jq}
│   ├── 1201_Webparse_ExternalAPI, 1202_KakaomapAPI_and_JQMobile
│   ├── dec08_{1_njst, 2_mdbnjs, 3_websocketsrv}   # Node.js
│   ├── dec09_{1_canva, 2_nodebackend, 2_tomfront, 2_uvicornback}
│   └── dec10_es6
├── C03_Newweb/                     # 15 subdirs (Dec–Jan)
│   ├── PIVOT/                      # ⭐ 풀스택 SNS (FastAPI + React)
│   │   ├── pivot_back, pivot_front, .github
│   ├── Reference/{MS_AISA, MS_AISA_BackEnd}
│   ├── dec10~dec24/*               # React/Vite, Redux, Socket.io, JWT, Ajax
│   └── jan13/testproject001
├── C04_AI/                         # 8 subdirs (Jan–Feb)
│   ├── Feb03_AzureAI               # GPT, DALL-E
│   ├── Feb04_azureAI               # Vision, Speech
│   ├── Feb05_Azure_Language        # Translation, Language Detection
│   ├── Jan27_base, Jan28
│   ├── Jan29_tf, Jan30_tf          # TensorFlow, PyTorch
├── Instructions/                   # 본 작업 지시문 (정비 대상 아님)
├── MS_AISA 12~18/                  # 팀 캡스톤 프로젝트 사본 7세트
│   └── MS_AISA 18/{MS_AISA, MS_AISA_BackEnd/{kwon, member, sns}}
├── Setup/                          # 환경 설정 파일
├── ejp_lib/                        # 커스텀 유틸 (DB·문자열·HTML·jQuery)
├── hangul-utils-master/            # 외부 한국어 NLP 라이브러리 (서드파티)
├── leeKNNModel/                    # KNN 모델 아티팩트 (.pkl)
├── misc/                           # 이미지·PDF·시험 자료 등 비코드
├── templates/{ThreeKingdoms}       # Flask/Jinja 템플릿
├── workspace6/                     # Eclipse 워크스페이스 (IDE 아티팩트)
│   ├── .metadata/{.config, .plugins}
│   └── General/{.dbeaver, .settings, Scripts}
├── 교재/                           # ⚠ 수업 교재 의심 (11개 하위)
│   ├── 01_Python, 02_OracleDB, 03_Node.js
│   ├── 04_DB/{01 - newDB}, 05_웹기초, 06_React, Svelte
│   ├── 07_Linux, 08_Azure, 09_Azure Machine Learning
│   └── 10_AI, 11_Azure AI
├── [루트 CSV] subway, lnps, titanic, seoul_air_quality, 모기예보 등
├── [루트 파일] 25-3-super-compressed_v1-2.pdf, .lnk 바로가기 2개
└── README.md (30바이트 플레이스홀더)
```

## 2. 최상위 디렉토리 한 문장 요약

| 디렉토리 | 요약 |
|---|---|
| `C01_python/` | 파이썬 기초 → 컬렉션·함수·OOP·MVC → Oracle·MongoDB·크롤링·NumPy/Pandas/Matplotlib·Jan 후반 ML 입문 (30 subdirs). |
| `C02_web/` | HTML/CSS/JS 기초 → Flask/FastAPI → Node.js(Express·WebSocket·Canvas) → 외부 API 연동 (21 subdirs). |
| `C03_Newweb/` | React/Vite + Redux, JWT, Socket.io, Ajax 학습 및 `PIVOT/` 풀스택 SNS 캡스톤. |
| `C04_AI/` | k-means·KNN·ANN·DNN·TensorFlow·PyTorch 그리고 Azure AI(GPT·DALL-E·Vision·Speech·Translation). |
| `Instructions/` | 본 정비 작업의 지시문 (작업 입력물, 정비 대상 아님). |
| `MS_AISA 12~18/` | 팀 캡스톤 프로젝트 7개 스냅샷. 18번이 가장 완성도 높음 (membership/kwon/sns 백엔드 + React 프론트). |
| `Setup/` | 환경 설치 관련 스크립트/설정. |
| `ejp_lib/` | Eric이 직접 작성한 재사용 유틸 (DB 매니저·문자열 클리너·템플릿). |
| `hangul-utils-master/` | 서드파티 한국어 NLP 라이브러리 복사본 — 재배포 여부 검토 필요. |
| `leeKNNModel/` | 사전 학습 KNN 모델 pickle + 설정. |
| `misc/` | 이미지·미디어·PDF(상공회의소 시험문제 등 포함)·깃허브 바로가기. 코드 아님. |
| `templates/` | Flask/Jinja HTML 템플릿 (수업 실습용). |
| `workspace6/` | Eclipse IDE 워크스페이스 메타데이터 — 공개 가치 없음. |
| `교재/` | **수업 교재/슬라이드 의심** 11개 하위 디렉토리. 저작권 리스크 최상위. |

## 3. 6개 모듈 매핑 체크리스트

| # | 모듈 | 매핑 경로 | 상태 |
|---|---|---|---|
| ① | AI 기초 프로그래밍 (Python·SQL·MongoDB) | `C01_python/1016–1031_*` (기초·OOP), `C01_python/1107_pyDBconn_*` (Oracle), `C01_python/1114_pyMongoDB/`, `C01_python/1110_*` (MVC) | ✅ **충실** |
| ② | 훈련용 데이터 구축 (크롤링·공공데이터) | `C01_python/1103_pyWebcrawl/`, `C02_web/1118_css_and_pyWebcrawl/`, `C02_web/1201_Webparse_ExternalAPI/`, `C02_web/1202_KakaomapAPI_*/` | ✅ **충실** |
| ③ | Full-stack 웹 개발 | `C02_web/*` (HTML/JS/Flask/FastAPI/Node), `C03_Newweb/dec10~dec24/*` (React·Redux·Socket·JWT), `C03_Newweb/PIVOT/` (FastAPI+React 풀스택) | ✅ **충실** — PIVOT이 Highlights 후보 |
| ④ | Azure 인프라 (VM·Linux·Cloud) | **코드 레포에 미발견.** `교재/07_Linux`, `교재/08_Azure` 존재하나 이는 교재 폴더 | ❌ **공백** — 사용자 확인 필요 |
| ⑤ | AI 기초 이론 (통계·CNN·RNN·GAN·KNN) | `C01_python/Jan26_ML/` (KNN), `C04_AI/Jan27_base/` (k-means), `C04_AI/Jan29_tf/` (ANN/DNN), `C04_AI/Jan30_tf/` (PyTorch), `leeKNNModel/` | ⚠ **부분** — CNN·RNN·GAN 산출물 불확실 |
| ⑥ | MS Azure AI (Copilot·OpenAI·Vision·NLP) | `C04_AI/Feb03_AzureAI/` (GPT·DALL-E), `C04_AI/Feb04_azureAI/` (Vision·Speech), `C04_AI/Feb05_Azure_Language/` (Translation·LangDetect) | ✅ **충실** |

**조치 필요**: 모듈 ④ 산출물 존재 여부를 사용자에게 확인. 로컬에만 있는 VM 스크린샷·Azure 포털 설정 기록 등이 있다면 Phase 2에서 별도 섹션으로 편입.

## 4. 문제점 분류 리스트

### 🔴 Critical — 공개 전 반드시 해결

**민감정보 (커밋된 시크릿)**
- [C04_AI/Feb03_AzureAI/1_gpt.py](C04_AI/Feb03_AzureAI/1_gpt.py) — Azure OpenAI `subscription_key`·deployment·endpoint 하드코딩
- [C04_AI/Jan27_base/1_msaml_client.py](C04_AI/Jan27_base/1_msaml_client.py) — Azure ML Bearer 토큰 하드코딩
- [C03_Newweb/PIVOT/pivot_back/.env](C03_Newweb/PIVOT/pivot_back/.env) — DB 자격증명 평문 (`ericjpark` / 비밀번호 / 내부 IP `195.168.9.138`)
- [C03_Newweb/dec17/2_FastAPI_back/.env](C03_Newweb/dec17/2_FastAPI_back/.env) — DB 자격증명 평문 (내부 IP `195.168.9.94`)
- `ejp_lib/ejpDBManager.py`, `C01_python/1110_pyOOP_mvc_airquality/…/SeoulAirQuality_Parser.py` — DB 접속 정보 하드코딩 흔적 (상세 검증 필요)

**저작권 의심 (수업 자료)**
- [교재/](교재/) 디렉토리 전체 (11개 하위: `01_Python` ~ `11_Azure AI`) — 파일명 정황상 강사 교재/슬라이드
- [교재/05_웹기초/](교재/05_웹기초/) 내 `.pptx` 4개 — 강의 슬라이드
- `25-3-super-compressed_v1-2.pdf` (1.4MB) — 파일명상 수업 자료 의심
- `misc/` 내 시험 PDF (상공회의소 시험문제 등)
- `hangul-utils-master/` — 서드파티 라이브러리 복사본 (라이선스 확인·필요 시 외부 링크로 대체)

**대용량 바이너리**
- [C01_python/Jan14_numpy/subway.csv](C01_python/Jan14_numpy/subway.csv) — 86MB
- `lnps.csv` (루트) — 55MB
- [leeKNNModel/model.pkl](leeKNNModel/model.pkl) — KNN pickle 모델

### 🟠 High

- **커밋된 `node_modules/`**: `C02_web/dec08_1_njst` (8MB), `dec08_2_mdbnjs` (27MB), `dec08_3_websocketsrv` (12MB), `dec09_1_canva` (14MB), `dec09_2_nodebackend` (12MB) 등 총 55 디렉토리·약 65MB
- **커밋된 `__pycache__/`**: 약 34곳
- **IDE 워크스페이스 커밋**: `workspace6/` (Eclipse 메타데이터), `.vscode/settings.json`
- **모듈 ④ 산출물 부재**: Azure 인프라 학습 흔적이 코드 레포에 없음 (교재만 있음)
- **핵심 디렉토리 README 부재**: `C01_python/`, `C02_web/`, `C03_Newweb/`, `C04_AI/`, `C03_Newweb/PIVOT/` 전부

### 🟡 Medium

- 루트 [README.md](README.md) 30바이트 (사실상 빈 파일)
- Raw 노트북 다수에 markdown 설명/맥락 부재 (`C04_AI/Jan29_tf/*`, `Jan30_tf/*` 등)
- 한/영 혼재 네이밍 (`C0X_python` vs `교재/01_Python`, `Jan27_base` vs `1103_pyWebcrawl`)
- `MS_AISA 12~18/` — 팀 프로젝트 7개 스냅샷 중복 — 어느 것이 "완성본"인지 미표기 (18이 가장 완성도 높아 보임)
- `hangul-utils-master/` 서드파티 라이브러리가 상위 레벨에 섞여 있음

### 🔵 Low

- Windows `.lnk` 바로가기 2개: `Parse_SeoulAirQuality - 바로 가기.lnk`, `navernews - 바로 가기.lnk`
- `.DS_Store` 가능성 (확인 필요)
- 파일명 규칙 불일치 (날짜 prefix 형식 혼재: `1015_`, `Jan14_`, `dec08_`, `Feb03_`)
- `C01_python/1113_nothing/` — 내용 없음 추정 (디렉토리명이 시사)

## 5. Highlights 후보 (사용자 선정용 초안)

Phase 2 루트 README `Highlights` 섹션에 3–5개를 선정해 게시할 예정. 근거 한 줄과 함께 추천:

1. **PIVOT — Full-Stack SNS** — [C03_Newweb/PIVOT/](C03_Newweb/PIVOT/)
   FastAPI + SQLAlchemy + SQLite 백엔드, React/Vite 프론트. 세션 인증·프로필 이미지 업로드·게시글/댓글 CRUD 포함. 캡스톤 수준.
2. **Seoul Air Quality MVC** — [C01_python/1110_pyOOP_mvc_airquality/](C01_python/1110_pyOOP_mvc_airquality/)
   공공 API → XML 파싱 → Oracle 저장 → CSV 산출. 실제 데이터 파이프라인 + OOP/MVC 분리.
3. **Azure AI 통합 스위트** — [C04_AI/Feb03_AzureAI/](C04_AI/Feb03_AzureAI/), [C04_AI/Feb04_azureAI/](C04_AI/Feb04_azureAI/), [C04_AI/Feb05_Azure_Language/](C04_AI/Feb05_Azure_Language/)
   Vision(OCR)·Speech(STT/TTS)·Translator·LangDetect·GPT·DALL-E 등 Azure Cognitive Services SDK 8종 실습.
4. **ML 진행 노트북 세트** — [C01_python/Jan26_ML/](C01_python/Jan26_ML/), [C04_AI/Jan27_base/](C04_AI/Jan27_base/), [C04_AI/Jan29_tf/](C04_AI/Jan29_tf/), [C04_AI/Jan30_tf/](C04_AI/Jan30_tf/)
   KNN → k-means → ANN → DNN → PyTorch 개념 진행 과정.
5. **React + Redux 멀티페이지** — [C03_Newweb/dec24/1_redux/](C03_Newweb/dec24/1_redux/), [C03_Newweb/dec23/react_front_multipage_1/](C03_Newweb/dec23/react_front_multipage_1/)
   Redux 상태관리 + 다페이지 라우팅 구조.

## 6. Phase 2 작업 제안

지시문 Phase 2 순서를 따르되, 본 조사 결과를 반영한 구체 제안:

### Step 1. Critical 선처리
1. ~~API 키/시크릿 **즉시 rotate**~~ → **CLOSED (2026-04-20)**: Azure 계정이 교육과정 종료로 잠김 → rotate 불가능·불필요. 리소스 동결로 키 실질 무효화.
2. `.env` 파일 삭제 + `.gitignore` 추가. `.env.example`로 치환.
3. 하드코딩된 키를 코드에서 제거하고 `os.getenv()` 또는 Azure Key Vault 패턴으로 교체.
4. **Git history 정화**: 현 커밋 수정만으로는 history에 시크릿이 잔존. `git filter-repo` 또는 BFG가 필요. **자동 실행 금지** — 사용자 판단·백업 후 별도로 진행.

### Step 2. 저작권 의심 자료 검토 (사용자 판단)
`교재/`, `25-3-super-compressed_v1-2.pdf`, `misc/` 내 시험 PDF, `hangul-utils-master/` 각각 **삭제 / 유지 / 요약후삭제** 중 선택. 판단 전까지 손대지 않음.

### Step 3. 대용량 바이너리 & 빌드 아티팩트 정리
- `node_modules/` 55개·`__pycache__/` 34개·`workspace6/`·`.vscode/` → 삭제 + `.gitignore` 등록
- `subway.csv` (86MB)·`lnps.csv` (55MB) → 삭제 후 "원본 출처 링크만 유지" 또는 Git LFS 전환
- `leeKNNModel/model.pkl` → 유지 여부 사용자 판단 (재현 가능성 vs 용량)

### Step 4. 모듈 재구성
```
modules/
  01-foundations/       ← C01_python/* (기초·OOP·DB·크롤링·NumPy·Pandas)
  02-data-ingestion/    ← 크롤링·공공API 관련 서브디렉토리
  03-fullstack/         ← C02_web/ + C03_Newweb/*
  04-azure-infra/       ← (공백 — 사용자에게 자료 제공 요청)
  05-ai-theory/         ← C04_AI/Jan27~Jan30/, C01_python/Jan26_ML/
  06-azure-ai/          ← C04_AI/Feb03~Feb05/
```
`git mv` 사용하여 history 보존. `MS_AISA 12~18/` 은 `team-projects/` 또는 Module ③ 하위로 배치.

### Step 5. 각 모듈 README 생성
지시문 템플릿 사용. **공백 채우기 금지** 원칙 엄수.

### Step 6. 노트북 output 선별 정리
원칙은 **보존**. 제거 대상: API 키 에코·개인정보·수천 행 데이터 덤프.

### Step 7. 루트 README 작성
기간·수료 증빙 블록·6개 모듈 맵·Highlights(3~5개)·SOHOBI 링크(`https://github.com/ProfessionalSeaweedDevourer/SOHOBI`) 포함.

### Step 8. `.gitignore` 점검, LICENSE(MIT 권장) 추가

### Step 9. Dry-run 요약 후 commit 승인 대기

## 7. Git History 오염 보고

현 워킹 디렉토리에서 파일을 삭제해도 **커밋 히스토리에는 시크릿/대용량 파일이 남는다**. 공개 리포로 전환 시 GitHub 이전 커밋을 누구나 조회 가능.

**영향 대상**:
- 하드코딩된 Azure API 키·Azure ML 토큰 (`C04_AI/Feb03_AzureAI/1_gpt.py`, `C04_AI/Jan27_base/1_msaml_client.py`)
- `.env` 파일 2개 (DB 자격증명)
- 대용량 바이너리(`subway.csv` 86MB, `lnps.csv` 55MB, `node_modules/` 55세트)

**권고**:
1. ~~Azure 포털에서 해당 키를 **즉시 rotate**~~ → **CLOSED (2026-04-20)**: 계정 잠금으로 rotate 불가능·불필요.
2. `git filter-repo` 또는 BFG Repo-Cleaner로 history 재작성 (force-push 필요). **자동 실행 금지.** 사용자 판단·백업 후 별도 단계에서 수동 실행.
3. 정화 후 공개 전환.

---

## 필수 질문 (Phase 1 종료 시 지시문 규정)

Phase 2 진입을 위해 다음 5개 응답이 필요하다. 별도 AskUserQuestion 프롬프트로 발송.

1. **AI-900 자격증·수료증 스캔본**: 로컬 존재 여부 및 리포지토리 포함 의사
2. **영어 README 병기 정책**: 한국어만 / 한국어+영어 / 영어만
3. **`교재/` 및 의심 PPT·PDF 처리**: 각 항목별 삭제 / 유지 / 요약후삭제
4. **LICENSE**: MIT 채택 여부
5. **Phase 2 commit 전략**: 단일 PR / 모듈별 분리 / Critical-Structure-Content 3단계 분리

**추가 긴급 사안** → **CLOSED (2026-04-20)**: Azure 계정이 교육과정 종료로 잠김. rotate 불가능하지만 리소스 동결로 키 실질 무효화. history redact는 위생 목적으로 Phase 2 Step 2에서 수행.

---

**Phase 1 종료. Phase 2 실행은 위 5개 질문 응답 후.** (키 rotate 조건은 Azure 계정 잠금으로 무효 종결)

---

## 사용자 응답 (2026-04-20)

| 항목 | 결정 |
|---|---|
| AI-900 자격증·수료증 스캔본 | **보유 + 포함** → Phase 2에서 `assets/`에 배치, 루트 README 상단 "수료 증빙" 블록에 이미지 게시 |
| README 언어 정책 | **한국어 + 영어 병기** → 루트·모듈 README 상단에 KO/EN 섹션 분리 작성 |
| LICENSE | **MIT** |
| Phase 2 commit 전략 | **Critical → Structure → Content 3단계 분리** |
| `교재/` | **삭제** (사용자가 로컬 외부로 이미 이동함) → Phase 2 Step 1에서 `git rm -r 교재/` |
| `25-3-super-compressed_v1-2.pdf` | **삭제** (사용자가 로컬 외부로 이동) → `git rm` |
| `misc/` 내 시험 PDF | **삭제** (이동 완료) → Phase 2에서 `misc/` 전수 검토 후 비저작권 자산만 `assets/`로 재배치 |
| `hangul-utils-master/` | **LICENSE 명시 후 유지** → 원 라이선스 파일 확인·보존, README에 출처·라이선스 표기 |

### Phase 2 긴급 선행 조치 (사용자 수동)

**CLOSED (2026-04-20)**: Azure 계정이 교육과정 종료로 잠김 → Azure OpenAI·Azure ML 키 rotate 불가능·불필요 (리소스 동결로 실질 무효화). DB 자격증명도 수업 실습 DB 종료로 동시 무효.

- **git history 정화**: `git filter-repo` 수동 실행 (백업 후), 공개 전환 전 완료 권장 — Phase 2 Step 2에서 수행

### Phase 2 Commit 단계 구성
1. **Critical**: 시크릿 제거, `.env` 삭제 + `.env.example`, `.gitignore` 정비, `node_modules`·`__pycache__`·`workspace6`·`.vscode` 삭제, 대용량 CSV·`model.pkl` 처리 결정, `교재/` `25-3-...pdf` `misc/` 시험 PDF 제거
2. **Structure**: `modules/01~06` 디렉토리 생성 후 `git mv`로 파일 이동, `MS_AISA 12~18` 정리, `hangul-utils-master` LICENSE 확인·`third-party/` 이동 검토
3. **Content**: 루트 README(KO+EN, 수료 증빙 블록, 6개 모듈 맵, Highlights, SOHOBI 링크), 각 모듈 README, LICENSE(MIT), 노트북 output 선별 정리
