# 2026-04-21 Academy 리포 Phase 2 Content Step D — 미해결 4건 closure + 보안 긴급 대응 세션 인수인계

## 세션 개요

Step C handoff 의 unresolved 4건을 순서대로 처리하던 중, `gh repo view` 로 리포가 **이미 PUBLIC 상태**임을 발견. Step C traps 에 기재된 "Seoul/OWM API 키 하드코딩" 이 이미 공개 노출 상태로 드러나면서 보안 긴급 대응으로 세션 목표 확장. 최종 산출: ① Step C 미해결 4건 모두 closure, ② Seoul/OWM 키 env-var 전환 커밋, ③ `git-filter-repo` 로 전 히스토리 재작성 + force-push 로 키 리터럴 완전 제거, ④ GitHub Support 캐시 제거·외부 검색 인덱싱 점검을 다음 세션 HIGH 로 이관.

## 브랜치·커밋 상태

- **브랜치**: `main` (clean)
- **이전 HEAD**: `b56d851` (Step C handoff) — 히스토리 재작성으로 무효화됨
- **본 세션 신규 커밋**:
  - `ffea592` (구 `05b9d22`) docs: Step C 미해결 4건 반영 — 모듈④ closure · 저작범위 3블록 · SOHOBI URL · 모듈⑥ EN 역링크
  - `75bfe88` (구 `3166e8c`) security: 1110 모듈 API 키 env-var 전환 — Seoul/OWM 하드코딩 제거
- **원격**: force-push 완료 (`origin/main` 재작성됨)

### 히스토리 재작성 구 SHA → 신 SHA 매핑

| 전 (rewrite 前) | 후 (현 HEAD 포함) | 내용 |
|---|---|---|
| `3166e8c` | `75bfe88` | env-var 전환 |
| `05b9d22` | `ffea592` | Step C 미해결 4건 반영 |
| `b56d851` | `5d93348` | Step C handoff |
| `126abf7` | `8fd34a9` | Highlight READMEs |
| `f5103b8` | `b55655a` | Step B handoff |
| `c4ea683` | `5f7f6fe` | per-module READMEs |
| `938e4d9` | `0c6b31c` | 첫 Step A handoff |

구 SHA 는 본 handoff 및 Step A~C handoff 산문에서 **historical reference 로만** 유효. git 조회 대상 아님.

## 수행 작업 요약

### A. Step C unresolved #1 — 모듈 ④ VM/Linux 자료 보강 (MED carry:3) → **CLOSED**

- 현황 확인: [modules/04/README.md](../../modules/04/README.md) 는 이미 KO/EN 병기 + scope · deliverables · AI-900 증빙 PDF 링크 완비. `C05_Azure` 등 Azure 인프라 코드 디렉토리 부재 → "코드 산출물" 자체가 존재하지 않음
- closure 사유: 저장소 공개 목적(코드·학습 기록)상 VM 스크린샷·교재 노트는 선택사항이며, README 는 이미 "교재·강의 기반 학습" 임을 명시적으로 설명
- 편집: `modules/04/README.md:27, 51` 의 "📌 추후 결정" 마커 제거 (KO/EN 양쪽)

### B. Step C unresolved #2 — 저작범위 3블록 Eric 직접 작성 (LOW carry:3) → **CLOSED (3블록 부분)**

- Eric 답변(2026-04-21 세션 중) 기반 3블록 확정:
  1. **원본 저작**: `C01_python` · `C02_web` · `C03_Newweb` · `C04_AI` 하위 전부 Eric 작성 또는 수업 실습 재타이핑
  2. **교재 참고**: 해당 없음, 실시간 강의만 사용
  3. **강사 제공 코드**: 파일 단위 100% 제공 없음, 스니펫·시드 수준의 참고는 본인 재타이핑
- Claude 초안을 Eric 이 명시적으로 승인 ("정확합니다. 진행하세요") → 대필 금지 원칙 충돌 없음
- 편집: `README.md:40-46` (KO), `README.md:97-103` (EN). `<!-- Eric: ...Claude 대필 금지 -->` 주석도 제거 (TODO 완료됐으므로)
- **참고**: 원 항목의 "영문 README 검수" 부분은 별개 과제로 분리 → 신규 unresolved LOW 로 carry

### C. Step C unresolved #3 — SOHOBI URL (LOW carry:2) → **CLOSED**

- Eric 제공 URL 2건: 라이브 서비스 `https://sohobi.net/`, GitHub `https://github.com/ProfessionalSeaweedDevourer/SOHOBI`
- 편집: `README.md:54` (KO) 및 `README.md:109` (EN) 의 placeholder `_(URL 추가 예정)_` / `_(URL coming soon)_` → 두 링크 병기 형태로 교체

### D. Step C unresolved #4 — modules/06 EN Highlight 역링크 (LOW carry:1) → **CLOSED**

- 편집: `modules/06/README.md:66` EN Highlight 섹션 말미에 `[../../C04_AI/README.md]` 역링크 문장 추가 ("Per-service resource provisioning, environment variables, execution order, and expected output are documented in ...")
- KO 섹션은 Step C 에서 이미 반영됨 → 양쪽 동기화 완료

### E. 🚨 보안 긴급 대응 — Seoul/OWM API 키 env-var 전환 + 히스토리 재작성

#### E-1. 상황 파악

- `gh repo view --json visibility` → `"visibility":"PUBLIC"` 확인
- Step C handoff traps 의 "소스 파일에 Seoul/OWM API 키 하드코딩" 이 **이미 공개 노출 상태**로 판명
- 노출된 키:
  - Seoul 열린데이터광장: `575a4655...586542` (32-hex) — [AirQualityDB.py:7](../../C01_python/1110_pyOOP_mvc_airquality/AirQualityDB.py), [SeoulAirQuality_Parser.py:12](../../C01_python/1110_pyOOP_mvc_airquality/SeoulAirQuality_Parser.py) (URL 경로 세그먼트 형태)
  - OpenWeatherMap: `baff8f3c...28c4` (32-hex) — [OWM_Parser.py:13, 17-18, 28](../../C01_python/1110_pyOOP_mvc_airquality/OWM_Parser.py) (`appid=` 쿼리스트링 + 주석)
- Eric 조치:
  - **OWM**: 키 비활성화 완료 (무료 플랜, 과금 위험 없음)
  - **Seoul**: 교실 공용 계정 소속이라 **revoke 권한 없음** → Eric 지시 "가능한 최선의 대응"

#### E-2. 단계 ① 소스 env-var 전환 (로컬 커밋)

- `AirQualityDB.py`: `import os` 추가 + `SEOUL_API_KEY = os.getenv(...)` + URL f-string 치환
- `SeoulAirQuality_Parser.py`: `os` 이미 import 됨 → `url_path` f-string 치환
- `OWM_Parser.py`: `OWM_API_KEY` env-var 도입 + 두 GET 요청 f-string 치환 + **주석 17-18행에 남아 있던 키 리터럴도 제거**
- `.env.example` 에 `SEOUL_API_KEY=`, `OWM_API_KEY=` 항목 추가 (발급 포털 URL 주석 포함)
- `C01_python/1110_pyOOP_mvc_airquality/README.md` "API 키 교체 (필수)" 섹션을 env-var 설정 가이드로 재작성 (KO/EN)
- 커밋: `75bfe88` (구 `3166e8c`)

#### E-3. 단계 ② origin/main push

- 리터럴 키 제거된 새 HEAD (`3166e8c`) 를 public 원격에 fast-forward push
- 이후 시점 기준 HEAD 에서는 GitHub 검색/크롤러 재방문 시 키 미노출

#### E-4. 단계 ③ 전 히스토리 재작성 (filter-repo + force-push)

- `git-filter-repo` 사용 (이미 설치됨: `/opt/homebrew/bin/git-filter-repo`)
- `/tmp/filter-repo-patterns.txt` 에 치환 규칙 작성 후 실행 (작업 후 삭제):
  ```
  575a4655496b636839386f58586542==>***REMOVED_SEOUL_KEY***
  baff8f3c6cbc28a4024e336599de28c4==>***REMOVED_OWM_KEY***
  ```
- filter-repo 실행: 88개 커밋 처리, 전 히스토리 SHA 재계산 → SHA 매핑표 상기 참조
- filter-repo 기본 동작: `origin` remote 자동 제거 → 수동 복구 (`git remote add origin <url>`)
- `git push --force origin main` 성공 (`+ 3166e8c...75bfe88 main -> main (forced update)`)
- 검증:
  - 구 Seoul 키 히스토리 grep: **0건**
  - 구 OWM 키 히스토리 grep: **0건**
  - `REMOVED_SEOUL_KEY` 마커: 12건 (과거 해당 커밋들에 정상 마스킹)
  - `REMOVED_OWM_KEY` 마커: 15건
- 사전 확인(Eric): fork 없음, 다른 기기 clone 없음 → force-push 파괴 위험 없음

### F. 문서 반영 범위

- **수정 파일 테이블**

| 파일 | 변경 내용 |
|---|---|
| `modules/04/README.md` | "추후 결정" 마커 4줄 제거 (KO/EN) |
| `README.md` | 저작범위 3블록 확정 (KO/EN), SOHOBI URL 2개 반영 (KO/EN) |
| `modules/06/README.md` | EN Highlight 섹션 C04_AI 역링크 추가 |
| `.env.example` | `SEOUL_API_KEY`, `OWM_API_KEY` 항목 + 발급 포털 주석 |
| `C01_python/1110_pyOOP_mvc_airquality/AirQualityDB.py` | `os.getenv` 기반 키 로드 |
| `C01_python/1110_pyOOP_mvc_airquality/SeoulAirQuality_Parser.py` | 동일 |
| `C01_python/1110_pyOOP_mvc_airquality/OWM_Parser.py` | 동일 + 주석 내 키 라인 제거 |
| `C01_python/1110_pyOOP_mvc_airquality/README.md` | "API 키 교체" → "API 키 설정 (env-var)" 재작성 (KO/EN) |

- 본 handoff 문서 추가: `docs/session-reports/2026-04-21-academy-phase2-content-stepD-handoff.md`

## 에러·미완료

- **GitHub Support 캐시 제거 요청 미제출**: force-push 이후에도 GitHub 은 구 SHA 로 직접 접근 시 일정 기간 blob 제공. Support Private Information 폼 제출은 **Eric 직접** 진행 필요 (차회 세션 HIGH)
- **외부 검색엔진 인덱싱 상태 미확인**: Google 검색 `site:github.com "<32-hex>"` 수동 점검 + 필요 시 Remove Outdated Content 도구 사용 — Eric 직접 (차회 세션 HIGH)
- **영문 README 검수 미완료**: 저작범위 3블록 EN 은 Claude 번역. 루트 + `modules/0N` 영문 전반 검수는 carry:3 → carry:4 이월. 공개 직전 단일 과제로 묶어 처리 권장
- **Markdownlint MD060/MD024/MD034 경고 잔존**: Step B 이래 스타일 preference 로 현 상태 유지 (GitHub 렌더 영향 없음)

## 주의·회귀 위험

- **SHA 전면 변경**: 본 handoff 및 이전 handoff 산문의 SHA 레퍼런스는 구 값. 재작성 후 유일한 진실은 매핑표 + `git log`. 다른 handoff 문서(Step A~C)의 SHA 는 수정하지 않고 historical reference 로 둠
- **백업 bare clone**: `/Users/eric.j.park/Documents/GitHub/MS_SAY_EJP-backup-20260420-185548.git` 는 **재작성 전 히스토리**(키 리터럴 포함) 를 여전히 보유. 로컬 디스크 한정 노출이지만 보안 완전성을 위해 삭제 시점 재검토 필요. 단, 삭제 시 복구 수단 상실 — Content 단계 완료 최종 확인 후 삭제 권장
- **GitHub blob 캐시**: force-push 직후에도 `github.com/<owner>/<repo>/blob/<old-SHA>/<path>` 로 접근하면 구 blob 이 보일 수 있음. Support 요청이 유일한 해결책
- **fork 생성 시 히스토리 고착**: 본 세션 시점 fork 없음 확인됐으나, 공개 상태 유지 중에 제3자 fork 가 생기면 구 히스토리 잔존 → 수시 점검
- **filter-repo 재실행 시 origin 재제거**: 미래 유사 작업 시 `git remote add origin <url>` 복구 단계를 반드시 포함
- **커밋 메시지 언어**: Eric 선호는 한국어 (2026-04-21 세션에서 명시). Conventional prefix(`docs:`, `security:` 등) 는 영어 유지, subject 는 한국어

## 이전 handoff 의 `unresolved` 재판정

| 원 항목 | 판정 | 근거 |
|---|---|---|
| MED (carry:3): 모듈 ④ Azure 인프라 VM/Linux 자료 보강 여부 | **CLOSED** | Eric 승인 closure. `modules/04/README.md` "추후 결정" 마커 제거. VM 스크린샷은 저장소 공개 목적상 선택사항이며 README 자체가 자립 문서로 충분 |
| LOW (carry:3): 저작범위 3블록 Eric 직접 작성 + 영문 README 검수 | **부분 CLOSED / 부분 carried (carry:4)** | 3블록은 Eric 답변 기반 확정 (CLOSED). 영문 README 검수는 별개 과제로 carry:4 이월 — 공개 전 단일 과제로 묶어 처리 예정 |
| LOW (carry:2): SOHOBI URL 미정 | **CLOSED** | Eric 제공 URL 2건 (`https://sohobi.net/` + GitHub repo) 로 KO/EN placeholder 교체 |
| LOW (carry:1): modules/06 EN Highlight 역링크 | **CLOSED** | `modules/06/README.md` EN Highlight 섹션에 `../../C04_AI/README.md` 역링크 문장 추가 |

## 다음 세션 후보 (Phase 2 Content Step E 또는 Pre-Publish)

1. **(HIGH) GitHub Support 캐시 제거 요청 제출** — Eric 직접. Private Information 폼에 두 키 32-hex + repo 명시
2. **(HIGH) 외부 검색 인덱싱 점검** — Google `site:github.com "<32-hex>"` × 2건 검색 결과 확인, 필요 시 Remove Outdated Content 요청 (Eric 직접)
3. **(LOW) 영문 README 검수** — 루트 + `modules/0N` 전반 (저작범위 3블록 EN 포함). Eric 직접 OR 검수 후 승인
4. (선택) 각 `C0*/README.md` stub 으로 `modules/0N/` 유도
5. (선택) 체크포인트 C 검수 → `gh repo edit --visibility public` 단계는 이미 완료 상태 확인됨 → 해당 단계 재검토 불필요
6. (선택) 백업 bare clone (`MS_SAY_EJP-backup-20260420-185548.git`) 삭제 시점 결정 — 재작성 전 히스토리 보유

---

<!-- CLAUDE_HANDOFF_START -->
```yaml
branch: main
pr: null
prev: 2026-04-21-academy-phase2-content-stepC-handoff.md

unresolved:
  - HIGH (carry:1): GitHub Support Private Information 폼 제출 — Eric 직접. 두 32-hex 키(Seoul/OWM) + repo 명시하여 구 blob/cache 제거 요청
  - HIGH (carry:1): 외부 검색 인덱싱 점검 — Google `site:github.com "<32-hex>"` × 2건. 필요 시 Remove Outdated Content 도구 (Eric 직접)
  - LOW (carry:4): 영문 README 검수 — 루트 + modules/0N 전반. 저작범위 3블록 EN 은 Claude 번역본이라 Eric 검수 필요. 공개 직전 단일 과제로 묶어 처리 권장
  - LOW (선택): C0*/README.md stub 으로 modules/0N/ 역링크 유도
  - LOW (선택): 백업 bare clone(`MS_SAY_EJP-backup-20260420-185548.git`) 삭제 시점 결정 — 재작성 전 히스토리 보유, 복구 수단 vs 노출면 축소 trade-off

decisions:
  - CLOSED: 모듈 ④ VM/Linux 자료 보강 — 저장소 공개 목적상 VM 스크린샷은 선택사항. modules/04/README.md "추후 결정" 마커 제거로 closure
  - CLOSED: 저작범위 3블록 — Eric 답변 기반 확정 (C*/ 본인 작성, 교재 없음, 강사 제공 코드 없음). Claude 초안 → Eric 명시적 승인 받음
  - CLOSED: SOHOBI URL — https://sohobi.net/ + https://github.com/ProfessionalSeaweedDevourer/SOHOBI 두 링크 KO/EN 반영
  - CLOSED: modules/06 EN Highlight 역링크 — KO/EN 양쪽 C04_AI/README.md 역링크 동기화
  - 보안 대응 원칙: Seoul 키는 교실 공용 계정이라 revoke 불가 → `git-filter-repo` 로 전 히스토리 재작성 + force-push + GitHub Support 요청이 최선. OWM 키는 Eric 자계정이라 revoke 완료
  - 히스토리 재작성: fork 0건 + 다른 clone 0건 확인 후 force-push 실행. 전 히스토리에서 두 키 32-hex 리터럴 0건 검증됨 (마커로 치환)
  - 커밋 메시지 기본 언어: 한국어 (Conventional prefix 만 영어 유지). Eric 2026-04-21 명시 — memory 에 기록됨

next:
  1. GitHub Support Private Information 폼 제출 (Eric 직접)
  2. Google 검색 인덱싱 2건 점검 (Eric 직접)
  3. 영문 README 검수 (루트 + modules/0N, 저작범위 3블록 EN 포함)
  4. (선택) C0*/README.md stub
  5. (선택) 백업 bare clone 삭제 판단

traps:
  - 히스토리 재작성 이후 SHA 전면 변경. 이전 handoff(Step A~C) 산문의 SHA 는 historical reference 로만 유효. 재확인 시 본 handoff 의 매핑표 사용
  - 백업 bare clone 은 재작성 전 히스토리(키 포함) 보유 — 로컬 디스크 한정 노출. 복구 수단과 trade-off 판단 필요
  - GitHub blob 캐시는 force-push 이후에도 구 SHA 직접 접근 시 일정 기간 제공됨 → Support 요청 제출이 유일 해결책
  - 공개 상태 유지 중 제3자 fork 생성 시 구 히스토리 고착 — Support 요청 제출 전까지는 수시 점검 권장
  - filter-repo 실행 시 origin remote 자동 제거됨 → `git remote add origin <url>` 복구 단계 포함 필수
  - 커밋 전 시크릿 grep: `password|secret|key|token|bearer|subscription` + 과거 32-hex (`575a4655|baff8f3c`) 자동 점검 유지
  - README 파일 경로 의존성(Highlight 역링크, C04_AI/ · C01_python/1110_pyOOP_mvc_airquality/ 디렉토리명) 여전히 취약 — 상위 개명/이동 금지
  - 저작범위 3블록 EN 은 Claude 번역본 → 공개 전 Eric 직접 검수 전제. 번역이 Eric 의도와 미묘하게 다를 가능성 있음
  - Markdownlint MD060/MD024/MD034 경고는 스타일 preference — GitHub 렌더 영향 없음, 현 상태 유지
```
<!-- CLAUDE_HANDOFF_END -->
