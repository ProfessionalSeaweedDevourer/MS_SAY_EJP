# 2026-04-21 Academy 리포 Phase 2 Content Step A — 루트 문서 세트 세션 인수인계

## 세션 개요

Phase 2 Content 1차분(루트 README·LICENSE·AI-900 수료증 배치)을 `main` 에 단일 커밋(`2ff3e16`)으로 반영. 세션 시작 시 `/boot` 로 이전 세션(Step 2) 컨텍스트 복원 → `/specify` 로 세션 스코프를 "루트 문서 최소 세트"로 좁혀(후보 A 선택) 모듈 재배치·모듈별 README·Highlights 독립 README는 다음 세션 이월. 저작 범위 3블록은 사용자 직접 작성 원칙 유지(TODO 마커만 삽입).

## 브랜치·커밋·원격 상태

- **브랜치**: `main`
- **이전 HEAD**: `37dc4f7` (Step 2 구조 정리 + force-push 완료 지점)
- **본 세션 커밋**: `2ff3e16 docs: add root README (KO+EN), LICENSE, AI-900 certificate assets`
- **원격 HEAD**: `2ff3e16` (GitHub API 조회로 로컬 일치 확인)
- **푸시 방식**: fast-forward (force-push 불필요)

## 수행 작업 요약

### A. 루트 문서 최소 세트 작성

| 파일 | 작업 | 비고 |
|---|---|---|
| [README.md](../../README.md) | UTF-16 30B placeholder → UTF-8 6.4KB 전면 재작성 | KO+EN 병기, 수료 증빙·6모듈 맵·Highlights 2건·저작범위 TODO·재현 가이드·SOHOBI placeholder |
| [LICENSE](../../LICENSE) | 신규 | MIT, `Copyright (c) 2024-2026 Joohyun "Eric" Park` (병기 형식, 사용자 확정) |
| [assets/ai900-certificate.pdf](../../assets/ai900-certificate.pdf) | 신규 복사 | 원본 295KB, `/Users/eric.j.park/Documents/인턴 지원용 자료/성적/ai900.pdf` 출처 |
| [assets/ai900-certificate.png](../../assets/ai900-certificate.png) | 신규 파생 | `sips -s format png` 1페이지 추출, 80KB, 792x612, README 인라인 표시용 |

### B. 수료증 PII 검토

`sips` 결과 PNG 시각 확인 후 사용자 승인:
- Joohyun Park / 2026-02-12 / verify code `wasv5-H9uQ` 모두 Microsoft 공식 수료증의 체용·검증 목적 공개 정보로 노출 문제 없음 결정.

### C. 모듈 링크 검증

README 내 상대 경로 전량 `ls` 확인. 최초 작성 시 `C01_python/1103_requests/` · `C02_web/1118_crawling/` 로 잘못 기재 → 실제 경로 `C01_python/1103_pyWebcrawl/` · `C02_web/1118_css_and_pyWebcrawl/` 로 KO/EN 양쪽 수정. 나머지 링크(`Jan26_ML`, `Feb03_AzureAI`, `1110_pyOOP_mvc_airquality`, `.env.example`, `PLAN.md`, `Instructions/INSTRUCTIONS.md`) 정상.

### D. 시크릿 사전 점검

`git diff --cached -- README.md LICENSE | grep -iE 'password|secret|key|token|bearer|subscription'` → 0건.

## 에러·미완료

- **에러(복구 완료)**: `Write` 도구가 기존 UTF-16 LE README.md 를 덮어쓸 때 UTF-16 인코딩을 보존 → `file` 이 `data` 로 인식. `rm` 후 재작성으로 UTF-8 로 교체 완료. 관련 패턴은 feedback 메모리로 저장(`feedback_write_tool_encoding.md`).
- **CoreGraphics PDF 경고**: `sips` 실행 시 stderr 경고 1건 출력되었으나 PNG 정상 생성되어 기능 영향 없음.
- **미완료**: 저작범위 3블록 Eric 직접 작성, `modules/01~06` 재배치, 6모듈별 README, Highlights 2건 독립 README, SOHOBI URL 확정.

## 주의·회귀 위험

- **README 모듈 링크가 현재 경로(`C01_python/` 등)를 가리킴**: 다음 세션에서 `modules/01~06/` 로 `git mv` 재배치하면 링크 전량 깨짐. 재배치 커밋에 README 링크 업데이트를 반드시 **같은 커밋**에 포함해야 PR 시 diff 가 일관됨.
- **Markdownlint 경고(MD049, MD060, MD024)**: 스타일 preference(asterisk vs underscore, 테이블 pipe 공백, 다국어 중복 헤딩). GitHub 렌더에는 영향 없음. `.markdownlint.json` 정책을 원하면 별도 세션에서 일괄 수정.
- **README 의 SOHOBI 링크**가 `URL 추가 예정` placeholder 상태: 사용자 SOHOBI 저장소 URL 확정 후 KO/EN 양쪽 동시 갱신 필요.
- **백업 bare clone** (`/Users/eric.j.park/Documents/GitHub/MS_SAY_EJP-backup-20260420-185548.git`): 여전히 유지. Content 단계 전체(모듈 재배치·모듈별 README·Highlights README까지) 완료 후 사용자 승인 시 삭제.

## 이전 handoff 의 `unresolved` 재판정

| 원 항목 | 판정 | 근거 |
|---|---|---|
| HIGH: Phase 2 Content 전체(README·LICENSE·6모듈 README·Highlights 2개·AI-900 수료증·modules/01~06) | **부분 CLOSED** | README(KO+EN)·LICENSE·AI-900 cert 본 세션에서 완료(`2ff3e16`). 잔여 3항목(6모듈 README, Highlights 2건, modules/01~06 재배치)은 HIGH(carry:1)로 이월 |
| MED: 모듈 ④ Azure 인프라 산출물 공백 | **carried (carry:1)** | 본 세션 README 에 "교재 학습(코드 미공개)"로 표기했으나 VM/Linux 자료 제공 가능 여부는 사용자 결정 대기. 공개 전환 전 최종 결정 필요 |
| LOW: 저작범위 3블록 Eric 작성 + 영문 README 검수 | **carried (carry:1)** | README KO/EN 양쪽에 TODO 마커 삽입 완료. 실제 본문 작성·검수는 미수행 |

## 다음 세션 (Phase 2 Content Step B 후보)

1. `modules/01~06/` 디렉토리 신설 + 현 `C01_python`/`C02_web`/`C03_Newweb`/`C04_AI` 서브디렉토리 `git mv` 재배치
2. 위 커밋에 루트 README 모듈 링크 업데이트 동봉(경로 깨짐 방지)
3. 6개 모듈별 README(KO+EN) 초안
4. Highlights 2건 독립 README + 재현 가이드 (Azure AI Integration Suite · Seoul Air Quality MVC)
5. 저작 범위 3블록 Eric 작성 요청 → 반영
6. SOHOBI URL 사용자 확정 → README 갱신
7. 체크포인트 B 검수 → `gh repo edit --visibility public` (사용자 직접)

---

<!-- CLAUDE_HANDOFF_START -->
```yaml
branch: main
pr: null
prev: 2026-04-20-academy-phase2-step2-handoff.md

unresolved:
  - HIGH (carry:1): modules/01~06 디렉토리 신설 + git mv 재배치 — README 모듈 링크가 현 경로를 가리키므로 재배치 커밋에 README 업데이트 동봉 필수
  - HIGH (carry:1): 6개 모듈별 README(KO+EN) 초안
  - HIGH (carry:1): Highlights 2건 독립 README — Azure AI Integration Suite(C04_AI/Feb03~05), Seoul Air Quality MVC(C01_python/1110_pyOOP_mvc_airquality)
  - MED (carry:1): 모듈 ④ Azure 인프라 산출물 공백 — 본 세션 README 는 "교재 학습(코드 미공개)"로 표기, 자료 보강 여부 사용자 결정 대기
  - LOW (carry:1): 저작범위 3블록 Eric 직접 작성 + 영문 README 검수 — README KO/EN 양쪽 TODO 마커만 삽입됨
  - LOW: SOHOBI URL 미정 — 사용자 확정 후 KO/EN 양쪽 placeholder 교체

decisions:
  - 세션 스코프 원칙: Phase 2 Content 는 한 세션 단위로 더 쪼개 진행. Step A(루트 문서) → Step B(구조+모듈 README) → Step C(Highlights·SOHOBI) 순
  - 저작권자 표기: `Joohyun "Eric" Park` 병기 (사용자 확정) — 법적 본명(수료증) + 영문 닉네임 병기
  - AI-900 수료증 PII 공개 방침: 이름·발급일·verify 코드 모두 공개 유지(마스킹 없음) — Microsoft 공식 수료증의 체용·검증 목적 공개 정보
  - 수료증 포맷: PDF 원본 + `sips` 변환 PNG 병기 — README 인라인은 PNG, 원본 다운로드 링크는 PDF
  - README 언어 구성: KO+EN 병기, 직역 금지, 상단 앵커 스위치(🇰🇷/🇺🇸)
  - 모듈 ④ 표기: 공개 README 에서 "교재 학습(코드 미공개)"로 명시하고 링크 생략 — 추후 사용자 자료 제공 시 갱신
  - 저작범위 3블록: Claude 대필 금지 원칙 유지, TODO 마커만 삽입
  - CLOSED: Phase 2 Content 루트 문서(README KO+EN · LICENSE MIT · AI-900 수료증 assets) — 본 세션 `2ff3e16` 로 완료
  - CLOSED: README 인코딩 문제 — UTF-16 LE placeholder 를 rm 후 UTF-8 로 재작성, `file` 로 `UTF-8 Unicode text` 확인

next:
  1. modules/01~06 디렉토리 신설 + C01~C04 서브 git mv (README 링크 업데이트 동봉, 단일 커밋)
  2. 6개 모듈별 README(KO+EN) 초안
  3. Highlights 2건 독립 README + 재현 가이드
  4. 저작범위 3블록 Eric 작성 요청·반영
  5. SOHOBI URL 확정·갱신
  6. 체크포인트 B 검수
  7. gh repo edit --visibility public (사용자 직접)

traps:
  - Write 도구가 기존 파일의 UTF-16 인코딩을 보존 — 기존 파일 `file` 확인 후 UTF-8 아니면 `rm` 먼저, 그 뒤 Write
  - README 모듈 링크는 현재 디렉토리(`C01_python/` 등)를 가리킴 — modules/01~06 재배치 커밋에 반드시 README 링크 업데이트 동봉
  - `sips` 의 CoreGraphics PDF 경고는 stderr 에만 출력되고 PNG 생성에 영향 없음 — 무시해도 됨
  - SOHOBI URL · Module ④ 자료 · 저작범위 3블록은 모두 사용자 응답 대기 — 임의 대필·추측 금지
  - Markdownlint 경고(MD049/MD060/MD024)는 스타일 preference. GitHub 렌더에 영향 없으므로 현 상태 유지, 일괄 수정은 별도 세션에서
  - 백업 bare clone `/Users/eric.j.park/Documents/GitHub/MS_SAY_EJP-backup-20260420-185548.git` 는 Content 단계 전체 완료 전까지 삭제 금지
  - 커밋 전 `git diff --cached | grep -iE 'password|secret|key|token|bearer|subscription'` 자동 점검 (상위 원칙 유지)
```
<!-- CLAUDE_HANDOFF_END -->
