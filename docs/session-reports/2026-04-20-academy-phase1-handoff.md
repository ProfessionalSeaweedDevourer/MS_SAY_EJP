# 2026-04-20 Academy 리포 공개 정비 Phase 1 세션 인수인계

## 세션 개요

`Instructions/INSTRUCTIONS.md` 지시문에 따라 MS AI SW Academy 이수 기록 백업 리포지토리(`MS_SAY_EJP`)의 공개 포트폴리오 정비 작업을 시작한 첫 세션. Phase 1 실태 조사 완료 + 사용자 승인에 따른 `.env`/`.csv` git history 정화 및 `.py` 하드코딩 Azure 키 제거를 처리함.

## 브랜치·커밋·원격 상태

- **브랜치**: `main`
- **원격**: `https://github.com/ProfessionalSeaweedDevourer/MS_SAY_EJP.git` (private)
- **HEAD**: 본 세션에서 force-push로 원격 history 재작성 완료
- **이전 세션 대비 주요 커밋**: 1개 신규 (credential 제거)

세션 중 추가된 커밋 목록 (신구 역순):

```
Replace hardcoded Azure credentials with os.environ lookups
```

(이전 커밋들은 history 재작성으로 SHA 변경됨. 원본 `.env`·`.csv`·하드코딩 키는 전 커밋에서 제거·redact 처리됨)

## 수정·생성 파일

| 경로 | 종류 | 내용 |
|---|---|---|
| `PLAN.md` | 신규 (untracked) | Phase 1 실태 조사 보고서. 디렉토리 트리·6모듈 매핑·Critical/High/Medium/Low 분류·Highlights 후보·Phase 2 제안·사용자 응답 기록 |
| `C04_AI/Feb03_AzureAI/1_gpt.py` | 수정 (커밋됨) | 하드코딩 Azure OpenAI 키·엔드포인트를 `os.environ` 조회로 대체 |
| `C04_AI/Jan27_base/1_msaml_client.py` | 수정 (커밋됨) | 하드코딩 Azure ML Bearer 토큰·엔드포인트를 `os.environ` 조회로 대체 |
| `docs/session-reports/2026-04-20-academy-phase1-handoff.md` | 신규 (untracked) | 본 문서 |

## Git history 정화 내역

`git-filter-repo` 2회 실행.

**1회차 — 파일 경로 제거** (`--paths-from-file`, `--invert-paths`)
- `.env` 3개 경로 (현·과거 위치 전부)
- `.csv` 15개 경로 (현·과거 위치 전부)
- 결과: 81 commits → 77 commits (orphan 4개 제거), `.git` 146MB → 120MB

**2회차 — 텍스트 redact** (`--replace-text`)
- Azure OpenAI subscription key
- Azure ML Bearer 토큰
- Student ID 포함 Azure OpenAI 엔드포인트
- 개인 식별자 포함 Azure ML 엔드포인트
- 치환값: `***REDACTED_AZURE_...***`

**검증**: 전체 history grep에서 원본 키·식별 엔드포인트 0건 확인.

**원격 반영**: `git push --force origin main` 완료 (`34b21bc` → `6a9574c`).

## 에러·미완료 작업

### 에러
- 없음. filter-repo 2회·push 모두 정상 종료.

### 미완료 (의도된 중단)
- Phase 2 Structure/Content 단계 미실행: 사용자와 합의한 `Critical → Structure → Content` 3단계 중 Critical 일부만 이번 세션에서 처리. 나머지 Critical 항목(`node_modules/`·`__pycache__/`·`workspace6/`·`.vscode/`·대용량 `.pkl` 등) 미커밋.
- 사용자의 수동 로컬 삭제 247건 미커밋 상태 유지 (`MS_AISA 12~17`, `교재/`, `misc/` 등).

## 사용자 수동 조치 필요 사항 (세션 밖)

**CLOSED (2026-04-20)**: Azure 계정이 교육과정 종료로 잠김 → 키 rotate 물리적으로 불가능·불필요. 리소스 동결로 Azure OpenAI·Azure ML 키는 실질 무효화됨.
DB 자격증명(`ericjpark`)도 수업 실습 DB 종료와 함께 무효. 내부망 IP + 더미 비밀번호 방치 결정 유지.

## 다음 세션 인수 요약

1. **Phase 2 Critical 나머지 커밋**: working tree의 247 deletion + `node_modules`·`__pycache__`·`workspace6`·`.vscode`·`leeKNNModel/model.pkl` 처리 + `.gitignore` 신규 작성 + `.env.example` 플레이스홀더 추가.
2. **Phase 2 Structure**: `modules/01~06/` 디렉토리 신설 후 `git mv`로 기존 학습 폴더 재배치. `MS_AISA 12~17`는 working tree에서 이미 삭제됨 → `18`만 팀 프로젝트 대표로 보존 여부 사용자 확인.
3. **Phase 2 Content**: 루트 README(KO+EN, 수료증 블록, 6모듈 맵, Highlights, SOHOBI 링크) + 6개 모듈 README 작성 + MIT LICENSE 추가.
4. **Phase 3 Highlights**: 사용자가 선정한 2~3개 결과물에 독립 README·재현 가이드·스크린샷 추가.
5. Azure 계정 잠금으로 rotate 종결 — 공개 전환은 filter-repo history redact 완료 후 진행.

## 주의·회귀 위험

- **history 이중 재작성**으로 reflog·이전 tag 전부 rewrite됨. 옛 SHA (`34b21bc`, `9a2fd61`) 참조 불가. GitHub 원격도 force-push로 옛 history 소실 — 실질 백업 없음.
- `git-filter-repo`는 실행 후 `origin` 원격을 자동 제거함. 재실행 시 `git remote add origin ...` 선행 필수.
- 기본 `--path-glob` 패턴은 `/`를 가로지르지 않음. 차후 `.env`/`.csv` 재유입 시에도 `git ls-files` + `git log --all --name-only`로 전수 경로를 뽑아 `--paths-from-file` 사용 권장.
- `.DS_Store`·`.claude/`·`Instructions/`·`PLAN.md`가 현재 untracked. Phase 2 commit 시 선별 필요 (`Instructions/`는 작업 브리프이므로 `docs/` 이동 또는 커밋 여부 사용자 판단).
- PIVOT 백엔드 등에서 DB 접속 코드(`ejpDBManager.py`, `SeoulAirQuality_Parser.py`)의 하드코딩 여부 재검증 필요. 본 세션에서는 scan 결과 특이사항 없음으로 처리했으나 `1_gpt.py`·`1_msaml_client.py` 이외 추가 시크릿 잔존 가능성 0이라고 단언 불가.

---

<!-- CLAUDE_HANDOFF_START -->
```yaml
branch: main
pr: null
prev: null

unresolved:
  - HIGH: Phase 2 Critical 나머지(node_modules·__pycache__·workspace6·.vscode·model.pkl 제거 + .gitignore + .env.example) 미처리
  - HIGH: 사용자 수동 삭제 247건 (MS_AISA 12~17·교재·misc PDF) 미커밋 상태
  - MED: PIVOT DB 접속 코드(ejpDBManager.py·SeoulAirQuality_Parser.py) 하드코딩 재검증 미수행
  - MED: 모듈 ④ Azure 인프라 산출물 공백 — 사용자에게 VM/Linux 학습 흔적 자료 제공 가능 여부 질의 필요
  - MED: MS_AISA 18 팀 프로젝트 대표 보존 여부 미결정
  - LOW: Instructions/·PLAN.md·.DS_Store·.claude/ untracked 상태 처리 미결정

decisions:
  - commit 전략: Critical → Structure → Content 3단계 분리 (사용자 승인)
  - README 정책: 한국어 + 영어 병기
  - LICENSE: MIT
  - AI-900 수료증: 보유·포함 예정 (Phase 2에서 assets/ 배치)
  - 교재/·25-3-pdf·misc 시험 PDF: 완전 삭제 (사용자가 로컬 외부로 이동 완료)
  - hangul-utils-master: LICENSE 명시 후 유지
  - CLOSED: .env/.csv history purge — filter-repo 2회 실행·원격 force-push 완료
  - CLOSED: .py 하드코딩 Azure 키 — HEAD os.environ 전환 + history redact 완료
  - CLOSED: Azure 키 rotate — 계정 잠금(2026-04-20, 교육과정 종료)으로 실행 불가·불필요

next:
  1. Phase 2 Critical 나머지: .gitignore 신규 + node_modules/__pycache__/workspace6/.vscode/model.pkl 제거 + .env.example 추가 + 247 수동 삭제 커밋
  2. 추가 시크릿 스캔: PIVOT·ejp_lib·노트북 전체 재스캔
  3. Phase 2 Structure: modules/01~06 디렉토리 신설 + git mv 재배치 + MS_AISA 18 처리 결정
  4. Phase 2 Content: 루트/모듈 README(KO+EN) + MIT LICENSE + AI-900 스캔본 assets/ 배치
  5. Phase 3 Highlights 후보 선정 (PIVOT, Seoul Air Quality MVC, Azure AI 스위트 중 2~3개)
  6. 공개 전환 전 history redact 완료 확인 (Azure 키 rotate는 계정 잠금으로 무효 종결)

traps:
  - git-filter-repo는 실행 시 origin 원격을 자동 제거 → 재실행 전 `git remote add origin ...` 필수
  - filter-repo 후 reflog·이전 tag 모두 rewrite됨 → 백업 태그는 실효성 없음 (force-push 전 별도 bare clone 백업 권장)
  - --path-glob은 / 를 가로지르지 않음 → 재실행 시 `git log --all --name-only` 로 경로 전수 수집 후 --paths-from-file 사용
  - 공개 전환은 filter-repo history redact 완료 후 진행 (Azure 키 rotate는 계정 잠금으로 무효 종결)
```
<!-- CLAUDE_HANDOFF_END -->
