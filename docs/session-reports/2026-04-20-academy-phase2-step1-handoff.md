# 2026-04-20 Academy 리포 Phase 2 Step 1 — 추가 시크릿 재스캔·수정 세션 인수인계

## 세션 개요

`docs/session-reports/academy-phase2-instructions-20260420.md` **Step 1** 단독 실행 세션. Phase 1에서 놓친 외부 시크릿이 있는지 전체 재스캔하고, 발견 시 HEAD 수정 후 커밋까지 완료. filter-repo 재실행은 다음 세션 Step 2 직전 일괄 처리로 이월.

## 브랜치·커밋·원격 상태

- **브랜치**: `main`
- **원격**: 동일. 본 세션은 push 없음 (로컬 커밋만).
- **이전 HEAD**: `6a9574c` (Phase 1 최종)
- **현재 HEAD**: `5419c06` (본 세션 신규 커밋)
- **신규 커밋 1개**:

  ```
  5419c06 security: replace remaining hardcoded Azure keys with os.environ lookups
  ```

## 수정·생성 파일

| 경로 | 종류 | 내용 |
|---|---|---|
| [C04_AI/Feb05_Azure_Language/2_Language_1_langdetect.py](../../C04_AI/Feb05_Azure_Language/2_Language_1_langdetect.py) | 수정 | `key` 하드코딩 → `os.environ.get("AZURE_LANGUAGE_KEY")` / `AZURE_LANGUAGE_ENDPOINT` |
| [C04_AI/Feb05_Azure_Language/1_Translate_1_txt.py](../../C04_AI/Feb05_Azure_Language/1_Translate_1_txt.py) | 수정 | `AZURE_TRANSLATOR_KEY` / `_ENDPOINT` / `_REGION` |
| [C04_AI/Feb05_Azure_Language/1_Translate_2_file.py](../../C04_AI/Feb05_Azure_Language/1_Translate_2_file.py) | 수정 | `AZURE_TRANSLATOR_KEY` / `AZURE_TRANSLATOR_DOCUMENT_ENDPOINT` |
| [C04_AI/Feb04_azureAI/2_azurespeech_voicerecognition.py](../../C04_AI/Feb04_azureAI/2_azurespeech_voicerecognition.py) | 수정 | `AZURE_SPEECH_KEY` / `AZURE_SPEECH_REGION` |
| [C04_AI/Feb04_azureAI/3_tts.py](../../C04_AI/Feb04_azureAI/3_tts.py) | 수정 | 동일 |
| [C04_AI/Feb04_azureAI/4_translate.py](../../C04_AI/Feb04_azureAI/4_translate.py) | 수정 | 동일 |
| `docs/session-reports/2026-04-20-academy-phase2-step1-handoff.md` | 신규 | 본 문서 |

## 스캔 결과 요약

### 발견된 외부 시크릿 (수정 완료)

3개 Azure 리소스, 6개 파일, 3개 distinct 키:

- **`ejp-lang-feb05`** (Azure AI Language) — `1tqWEWX4…`
- **`ejp-translator-feb05`** (Azure Translator) — `5RgqlRwz…`
- **Azure Speech, `eastus2`** (리소스명 미확인) — `GEfSMR0n…`

### 방치 (사용자 정책에 따라)

Oracle `ericjpark/0000@195.168.9.X:1521/xe` 패턴 6건 (내부망 IP + 더미 비밀번호, 공개 시 실질 위협 없음):

- `ejp_lib/ejpDBManager.py`
- `C01_python/1110_pyOOP_mvc_airquality/ejp/ejpDBManager.py` (connect_string 파라미터화)
- `C01_python/1111_pyMVC_prac_webmall/MWM/ejp_lib/ejpDBManager.py`
- `C01_python/1112_pyMVC_expense/MyExpense/ejp_lib/ejpDBManager.py` (IP `.106`)
- `C01_python/Jan16_pd/4_oracledb.py` (IP `.99`)
- `C02_web/1125_JS_BMIcalc/NewWeb_Backend/lib/ejpDBManager.py` (IP `.207`)

### 오탐

- `workspace6/.metadata/…workbench.xmi` (Eclipse XML `key=` 속성, Step 2 삭제 예정)
- `node_modules/**` (Step 2 삭제 예정)
- `C04_AI/Jan27_base/2_kMeans_movie.ipynb` (matplotlib base64 이미지 출력)

## 사용자 수동 조치 필요 (세션 밖)

**CLOSED (2026-04-20)**: Azure 계정이 교육과정 종료로 잠김 → 키 rotate 물리적으로 불가능. 리소스 동결로 키는 실질 무효화됨. history redact(filter-repo)는 위생 목적으로 Step 2에서 수행.

## 에러·미완료

- 에러 없음. 커밋 정상 종료.
- 미완료(의도): filter-repo `--replace-text` 재실행은 Step 2 대형 정리 커밋 직전 일괄 처리 (3분할 합의 준수)

## 다음 세션 (Phase 2 Step 2)

Step 2 = Working tree 정리 단일 커밋. 지시문 기준:

1. `.gitignore` **갱신** (신규 작성 아님, 기존 파일 확인 필요): `__pycache__/`·`*.pyc`·`.ipynb_checkpoints/`·`.env`·`.env.*`·`!.env.example`·`venv/`·`.venv/`·`node_modules/`·`.vscode/`·`.DS_Store`·`workspace6/`·`*.pkl`
2. `.env.example` 신규 — 구 `.env` 2건에서 확인된 변수명 + 본 세션에서 확정된 Azure 환경변수명(`AZURE_LANGUAGE_KEY/ENDPOINT`, `AZURE_TRANSLATOR_KEY/ENDPOINT/REGION/DOCUMENT_ENDPOINT`, `AZURE_SPEECH_KEY/REGION`) 포함
3. 대형 `git rm -r`: `node_modules/` 55세트, `__pycache__/` 30곳(+이미 커밋된 총 7,592+ 파일), `workspace6/`, `.vscode/`, `leeKNNModel/model.pkl`, `hangul-utils-master/`, `C01_python/1113_nothing/`
4. working tree 247건 수동 삭제(`MS_AISA 12~18`, `교재/`, `misc/` 등) `git rm` 반영
5. `git-filter-repo --replace-text` 재실행 — **과거 커밋**의 6개 원본 키 redact (위 3개 + Phase 1의 3개, `***REDACTED_AZURE_…***` 치환)
6. 커밋 메시지: `chore: clean build artifacts, IDE files, vendored third-party, and reference team projects`
7. `git push --force origin main`
8. 체크포인트 A — 사용자 확인

## 주의·회귀 위험

- 본 세션 커밋(`5419c06`)은 아직 push 되지 않음. 다음 세션에서 Step 2 변경과 함께 일괄 push 권장.
- filter-repo 재실행 시 origin 자동 제거 → 재실행 전 `git remote -v` 확인, 필요 시 `git remote add origin ...`.
- Feb04 Speech 리소스의 **Azure 리소스명이 파일에 기록되지 않음** (키만 있고 region만 `eastus2`). 계정 잠금으로 식별 불필요.

---

<!-- CLAUDE_HANDOFF_START -->
```yaml
branch: main
pr: null
prev: 2026-04-20-academy-phase1-handoff.md

unresolved:
  - HIGH: Phase 2 Step 2 전체 (.gitignore 갱신·.env.example·node_modules/__pycache__/workspace6/.vscode/model.pkl·hangul-utils-master·MS_AISA 18·working tree 247건 삭제 반영·filter-repo --replace-text 재실행·force-push)
  - MED: 모듈 ④ Azure 인프라 산출물 공백 — 사용자에게 VM/Linux 학습 흔적 자료 제공 가능 여부 질의 필요
  - LOW: Instructions/·PLAN.md·.DS_Store·.claude/ untracked 상태 처리 (Step 2에서 일괄 결정)

decisions:
  - commit 전략: Critical → Structure → Content 3단계 분리, 세션 당 1단계 (사용자 승인)
  - README 정책: 한국어 + 영어 병기 (직역 금지)
  - LICENSE: MIT
  - AI-900 수료증: assets/ 배치
  - 교재/·25-3-pdf·misc·MS_AISA 전 세트(18 포함): 완전 삭제 (지시문 확정)
  - hangul-utils-master: 삭제 (지시문 확정, 서드파티 벤더링 취소)
  - Highlights 2개: Azure AI Integration Suite + Seoul Air Quality MVC (PIVOT 제외)
  - 내부망 IP + 더미 비밀번호(195.168.x.x / "0000"): 공개 시 실질 위협 없음으로 방치
  - CLOSED: .env/.csv history purge — Phase 1 filter-repo 2회·force-push 완료
  - CLOSED: Phase 1 .py 하드코딩 Azure 키 (Feb03 GPT·Jan22 ML) — os.environ 전환 + redact 완료
  - CLOSED: Phase 2 Step 1 추가 시크릿 재스캔 — Feb04/Feb05 6파일 os.environ 전환 커밋(5419c06), history redact는 Step 2 직전 일괄
  - CLOSED: Azure 키 rotate (5건) — 계정 잠금(2026-04-20, 교육과정 종료)으로 실행 불가·불필요. 리소스 동결로 키 실질 무효화

next:
  1. .gitignore 갱신 (기존 파일에 Step 2 항목 추가)
  2. .env.example 신규 (Feb04/Feb05 환경변수 + 구 .env 변수명)
  3. 대형 git rm -r (node_modules 55·__pycache__ 30·workspace6·.vscode·leeKNNModel/model.pkl·hangul-utils-master·C01_python/1113_nothing·MS_AISA 18·working tree 247건)
  4. 커밋: chore: clean build artifacts, IDE files, vendored third-party, and reference team projects
  5. git-filter-repo --replace-text — 과거 커밋 6개 원본 키 redact
  6. force-push + 체크포인트 A
  7. (이후 세션) Structure → Content

traps:
  - 본 세션 커밋 5419c06은 push 미전송 — Step 2에서 일괄 push
  - git-filter-repo 실행 시 origin 원격 자동 제거 → 재실행 전 `git remote -v` 확인·필요 시 `git remote add origin ...`
  - filter-repo 후 reflog·tag rewrite됨 → 백업 태그 실효성 없음, force-push 전 별도 bare clone 백업 권장
  - --path-glob은 / 를 가로지르지 않음 → 재실행 시 `git log --all --name-only`로 경로 전수 수집 후 --paths-from-file 사용
  - 공개 전환은 filter-repo 재실행·history redact 완료 후 진행 (Azure 키 rotate는 계정 잠금으로 무효 종결)
  - 커밋 전 매번 `git diff --cached | grep -iE 'password|secret|key|token|bearer|subscription'` 자동 점검 (지시문 상위 원칙)
```
<!-- CLAUDE_HANDOFF_END -->
