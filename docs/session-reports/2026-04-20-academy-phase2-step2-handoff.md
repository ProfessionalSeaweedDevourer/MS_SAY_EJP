# 2026-04-20 Academy 리포 Phase 2 Step 2 — Structure 정리 + Azure 계정 잠금 반영 세션 인수인계

## 세션 개요

Phase 2 Step 2(Structure 정리) 전체 + Azure 계정 교육과정 종료로 잠금된 상황을 5개 문서에 반영하는 meta 정리 동시 수행. 세션 시작 시 사용자가 "Azure 계정 접근 불가(교육과정 종료)" 상황을 고지 → rotate 의무 조항을 전 문서에서 CLOSED 처리한 뒤 Step 2 대형 cleanup·filter-repo·force-push 진행.

## 브랜치·커밋·원격 상태

- **브랜치**: `main`
- **원격**: `https://github.com/ProfessionalSeaweedDevourer/MS_SAY_EJP.git` (private)
- **이전 HEAD (push 미전송 로컬)**: `5419c06`
- **Step 2 구조 정리 커밋 (filter-repo 전)**: `e171687`
- **filter-repo 후 HEAD**: `37dc4f7`
- **force-push 완료**: `6a9574c` → `37dc4f7` (원격도 `37dc4f7` 확인)

## 수행 작업 요약

### A. Azure 계정 잠금 반영 (5파일)

Azure 포털 접근 불가로 Azure OpenAI·Azure ML·Azure Language·Azure Translator·Azure Speech 5건 rotate가 물리적으로 불가·불필요. 모든 "사용자 수동 조치 — rotate" 의무 조항을 `CLOSED (2026-04-20): 계정 잠금으로 rotate 불가능·불필요. 리소스 동결로 실질 무효화` 로 표기.

| 파일 | 변경 |
|---|---|
| [docs/session-reports/2026-04-20-academy-phase2-step1-handoff.md](2026-04-20-academy-phase2-step1-handoff.md) | "사용자 수동 조치" 섹션 CLOSED 축약, YAML unresolved HIGH rotate 제거, decisions CLOSED 추가, traps 공개 전환 조건 수정 |
| [docs/session-reports/2026-04-20-academy-phase1-handoff.md](2026-04-20-academy-phase1-handoff.md) | 동일 방식 정리 |
| [docs/session-reports/academy-phase2-instructions-20260420.md](academy-phase2-instructions-20260420.md) | 공개 전환 체크 NOTE 추가 + 체크박스 N/A 표기 |
| [PLAN.md](../../PLAN.md) | 5개 지점 rotate 지시 CLOSED 표기 |
| `Instructions/INSTRUCTIONS.md` | rotate 키워드 없음 — 변경 없음 |

### B. Phase 2 Step 2 실행

**B-1/B-2 — `.gitignore` 갱신 + `.env.example` 신규**
- `.gitignore`: `__pycache__/`·`*.pyc`·`.ipynb_checkpoints/`·`.env`·`.env.*`·`!.env.example`·`venv/`·`.venv/`·`node_modules/`·`.vscode/`·`.DS_Store`·`workspace6/`·`*.pkl`·`.claude/` 추가 (기존 `EC2 Tutorial.pem` 보존).
- `.env.example`: Phase 1+2 Step 1 총 8개 변수(`AZURE_OPENAI_KEY/ENDPOINT/DEPLOYMENT/API_VERSION`, `AZURE_ML_KEY/ENDPOINT`, `AZURE_LANGUAGE_KEY/ENDPOINT`, `AZURE_TRANSLATOR_KEY/ENDPOINT/REGION/DOCUMENT_ENDPOINT`, `AZURE_SPEECH_KEY/REGION`) 플레이스홀더. 상단 주석에 계정 잠금 사실 명시.

**B-3/B-4 — 대형 삭제 + 구조 정리 단일 커밋 (`e171687`)**
- `git rm`: node_modules 7,517, __pycache__ 74, workspace6 59, .vscode 1, leeKNNModel/model.pkl 1, hangul-utils-master 13, C01_python/1113_nothing 1, MS_AISA 18 73, misc 13
- `git add -u`: 이미 working tree 삭제된 247건(`MS_AISA 12~17`, `교재/`, `25-3-super-compressed_v1-2.pdf`) D 상태 반영
- 신규 add: `.gitignore` 수정, `.env.example`, `docs/`, `Instructions/`, `PLAN.md`
- `git ls-files`: **8,962 → 1,062** (약 7,900 감소)
- diff stat: `7907 files changed, 30 insertions(+), 1369482 deletions(-)`
- 시크릿 사전 점검: `git diff --cached | grep -iE 'password|secret|key|token|bearer|subscription'` → placeholder 및 삭제된 JS 키워드 문서만 검출, 실제 시크릿 0건

**B-5 — bare clone 백업**
- `/Users/eric.j.park/Documents/GitHub/MS_SAY_EJP-backup-20260420-185548.git` (119M)

**B-6 — git-filter-repo --replace-text 재실행**
- 추출: `5419c06^` 커밋의 6개 `.py` 파일에서 Azure 키 3종 유니크 추출 (80~90자 패턴 매치)
- 임시 파일: `/var/folders/.../tmp.K2rBXkrGAl/replace.txt` (사용 후 `rm -rf`로 삭제 완료)
- 치환: `<key>==>***REDACTED_AZURE_KEY***`
- 결과: 80 커밋 재작성, HEAD `e171687` → `37dc4f7`, 원격 자동 제거 후 재추가
- 검증: 3개 키 8자 프리픽스는 **요약 섹션(fragment only)에만 잔존** — 전체 키 복원 불가, 실질 노출 없음

**B-7 — force-with-lease push**
- `git fetch origin main` → `git push --force-with-lease origin main` 성공
- 원격 HEAD: `37dc4f7` (LOCAL 일치 확인: `gh api repos/.../commits/main --jq .sha`)

**B-8 — 체크포인트 A**
- 원격 트리 최상위: 대형 디렉터리(`node_modules`, `workspace6`, `MS_AISA 12~18`, `교재`, `misc`, `hangul-utils-master`) 모두 사라짐 확인
- `Instructions/`, `PLAN.md`, `docs/`, `.env.example`, `.gitignore` 정상 반영 확인

## 에러·미완료

- 에러 없음. 전 단계 1회 실행으로 완료.
- 미완료: Phase 2 Content 단계 (README KO+EN, LICENSE MIT, 6개 모듈 README, AI-900 수료증 배치, Highlights) — 다음 세션 과제

## 주의·회귀 위험

- **백업 경로**: `MS_SAY_EJP-backup-20260420-185548.git` — filter-repo 이전 상태(`6a9574c`) 보존. Content 단계 완료 후 삭제 가능.
- **force-push 이후 reflog/태그 전량 rewrite** — 과거 SHA 참조 불가. 백업 bare clone 외에는 이전 상태 복원 수단 없음.
- **공개 전환 조건**: Azure 계정 잠금으로 rotate 요건은 N/A. 남은 조건은 (1) Content 단계 완료, (2) 저작 범위 블록 Eric 작성, (3) 영문 README 검수.
- **`.env.example` 실 사용 불가**: 모든 Azure 리소스가 계정 잠금으로 동결되어 키 발급 불가. 향후 공개 저장소 방문자가 재현하려면 본인 Azure 구독에서 동일 이름 환경변수로 키 주입 필요 — 주석에 명시 완료.

## 다음 세션 (Phase 2 Content)

1. 루트 `README.md` KO+EN (수료 증빙 블록, 6모듈 맵, Highlights 2개, SOHOBI 링크)
2. `LICENSE` MIT 추가
3. `modules/01~06/` 디렉토리 신설 후 `git mv`로 재배치 (Structure 일부 이월 작업)
4. 6개 모듈별 README (KO+EN)
5. AI-900 수료증 이미지 `assets/` 배치 + README 블록 연결
6. Highlights 2개 후보: Azure AI Integration Suite, Seoul Air Quality MVC
7. 공개 전환 (`gh repo edit --visibility public`) — 사용자 직접 실행

---

<!-- CLAUDE_HANDOFF_START -->
```yaml
branch: main
pr: null
prev: 2026-04-20-academy-phase2-step1-handoff.md

unresolved:
  - HIGH: Phase 2 Content 단계 전체 — 루트 README(KO+EN), LICENSE MIT, 6모듈 README, Highlights 2개, AI-900 수료증 배치, modules/01~06 디렉토리 재구성
  - MED: 모듈 ④ Azure 인프라 산출물 공백 — 사용자에게 VM/Linux 학습 흔적 자료 제공 가능 여부 질의 필요
  - LOW: 공개 전환 전 저작 범위 블록 3개 Eric 직접 작성 + 영문 README 검수 필요

decisions:
  - commit 전략: Critical → Structure → Content 3단계 분리, 세션 당 1단계 (사용자 승인)
  - README 정책: 한국어 + 영어 병기 (직역 금지)
  - LICENSE: MIT
  - AI-900 수료증: assets/ 배치
  - hangul-utils-master: 삭제 (Phase 2에서 재확인, 본 세션에서 git rm 완료)
  - Highlights 2개: Azure AI Integration Suite + Seoul Air Quality MVC (PIVOT 제외)
  - 내부망 IP + 더미 비밀번호(195.168.x.x / "0000"): 공개 시 실질 위협 없음으로 방치
  - `.claude/` 디렉토리: .gitignore에 추가 (커밋 대상 아님)
  - Instructions/·PLAN.md·docs/: 본 세션 구조 커밋에서 tracked 처리
  - CLOSED: Azure 키 rotate (5건) — 계정 잠금(2026-04-20, 교육과정 종료)으로 실행 불가·불필요. 리소스 동결로 키 실질 무효화
  - CLOSED: Phase 2 Step 1 추가 시크릿 재스캔 — Feb04/Feb05 6파일 os.environ 전환 (5419c06, filter-repo 후 0a2ca14로 rewrite)
  - CLOSED: Phase 2 Step 2 Structure 정리 — 8,962→1,062 파일, filter-repo --replace-text 3키 신규 redact, force-push 37dc4f7 완료
  - CLOSED: .env/.csv history purge — Phase 1 filter-repo 2회 완료 (SHA 이력은 본 세션 filter-repo로 재rewrite)

next:
  1. 루트 README(KO+EN) 초안 작성 — 수료 증빙 블록·6모듈 맵·Highlights 2개·SOHOBI 링크
  2. LICENSE MIT 파일 추가
  3. modules/01~06/ 디렉토리 신설 후 git mv 재배치
  4. 6개 모듈별 README(KO+EN)
  5. AI-900 수료증 assets/ 배치 + README 이미지 블록 연결
  6. Highlights 2개 독립 README + 재현 가이드
  7. 체크포인트 B — 사용자 검수
  8. gh repo edit --visibility public (사용자 직접)

traps:
  - 백업 bare clone 경로: /Users/eric.j.park/Documents/GitHub/MS_SAY_EJP-backup-20260420-185548.git (filter-repo 이전 상태, Content 단계 완료 후 삭제 가능)
  - git-filter-repo 실행 시 origin 원격 자동 제거 → 재실행 전 `git remote -v` 확인·필요 시 `git remote add origin https://github.com/ProfessionalSeaweedDevourer/MS_SAY_EJP.git`
  - filter-repo 후 reflog·tag rewrite됨 → 백업 bare clone 외 이전 상태 복원 수단 없음
  - Azure 모든 리소스 동결 상태 — .env.example 채워도 실 호출 불가능. 공개 후 재현자는 본인 구독에서 키 발급 필요
  - 공개 전환 전 저작 범위 블록 3개 Eric 직접 작성 필수 — Claude가 대필 금지 (지시문 상위 원칙)
  - 커밋 전 매번 `git diff --cached | grep -iE 'password|secret|key|token|bearer|subscription'` 자동 점검 (지시문 상위 원칙)
  - .env.example의 `AZURE_SPEECH_REGION` 기본값 `eastus2`는 실습 시 사용된 리전 — 새 구독에서는 사용자 선택 리전으로 변경 필요
```
<!-- CLAUDE_HANDOFF_END -->
