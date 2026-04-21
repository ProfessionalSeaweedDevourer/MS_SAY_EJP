# 2026-04-21 Academy 리포 Phase 2 Content Step B — 모듈별 README 논리 인덱스 세션 인수인계

## 세션 개요

Phase 2 Content Step B 를 `main` 에 단일 커밋(`c4ea683`)으로 반영 후 원격 푸시. 세션 시작 시 `/boot` 로 Step A 컨텍스트 복원 → `/specify` 에서 원안(`modules/01~06` 물리 재배치) 대신 **C안(논리 인덱스만 신설)** 으로 스코프 전환. `C01~C04` 물리 구조는 그대로 두고 `modules/0N/README.md` 6개가 실제 서브디렉토리 경로를 가리키도록 구성. 루트 README 모듈 표를 `modules/0N/` 링크로 교체.

## 브랜치·커밋·원격 상태

- **브랜치**: `main`
- **이전 HEAD**: `938e4d9` (Step A handoff 문서)
- **본 세션 커밋**: `c4ea683 docs: add per-module READMEs (modules/01~06) as logical index`
- **원격 HEAD**: `c4ea683` (fast-forward push 완료: `938e4d9..c4ea683`)
- **푸시 방식**: fast-forward

## 수행 작업 요약

### A. 방향 전환 판단 (A/B/C 3안 비교)

원안(Step A handoff `next` 1번: "modules/01~06 + git mv 재배치")을 분석 결과 단순 1:1 매핑 불가 판정:

- `C01_python/` 이 모듈 ①(Python 기초) · ②(크롤링 1103) · ⑤(Jan14~26 수치/ML) 세 모듈에 걸침
- `C02_web/` 이 모듈 ②(1118/1128/1201/1202) · ③(HTML/JS/FastAPI/Node) 에 걸침
- `C04_AI/` 가 모듈 ⑤(Jan27~30 TF) · ⑥(Feb03~05 Azure AI) 에 걸침

→ 서브디렉토리 단위 `git mv` 수십 개가 1 커밋에 몰리면 diff·리스크 큼. **C안 (논리 인덱스만 신설, 물리 구조 유지)** 채택.

### B. 모듈별 README 작성 (KO+EN 병기)

| 파일 | 내용 요약 |
|---|---|
| [modules/01/README.md](../../modules/01/README.md) | AI Foundations — `C01_python/1015~1114*` (1103 제외) |
| [modules/02/README.md](../../modules/02/README.md) | Data Ingestion — `C01_python/1103_pyWebcrawl` + `C02_web/1118, 1128, 1201, 1202` |
| [modules/03/README.md](../../modules/03/README.md) | Full-Stack Web — `C02_web/` 잔여 + `C03_Newweb/` 전체 |
| [modules/04/README.md](../../modules/04/README.md) | Azure Infrastructure — stub (교재 학습, 코드 미공개 명시) |
| [modules/05/README.md](../../modules/05/README.md) | AI Theory — `C01_python/Jan14~Jan26_ML` + `C04_AI/Jan27~30` |
| [modules/06/README.md](../../modules/06/README.md) | MS Azure AI — `C04_AI/Feb03~05` |

각 README 공통 섹션: 포함 디렉토리 표(상대 경로 `../../C0*/...`), 핵심 학습 주제, 재현 주의, 해당 모듈의 Highlight(①·⑥에만).

### C. 루트 README 모듈 표 링크 교체

`[README.md](../../README.md)` KO/EN 양쪽 모듈 표의 3번째 컬럼 "주요 경로/Primary Paths" → "상세 README/Detailed README" 로 변경하고 링크 대상을 `C0*/` 에서 `modules/0N/` 로 전환. 모듈 ④ 상태 표기를 `⚠️` → `⚠️ 교재 학습` 으로 명확화.

### D. 경계 판정

- `1103_pyWebcrawl` 은 시간순(C01_python 11월)으로는 ①, 주제로는 ②. **Module ②로 분류**, Module ① README 에 "시간순으로 이 구간이지만 주제상 ②" 라고 명시.
- `Jan22_Backup`, `Jan23_Backup` 실제 내부 확인(`ls`) 결과 각각 텍스트 처리(list·basic·special_chars·verbcount) · 텍스트/이미지. Module ⑤에 분류.
- `C03_Newweb/PIVOT` = `pivot_back` + `pivot_front` 풀스택 전환 프로젝트 → Module ③.
- `C03_Newweb/Reference` = 강사 제공 MS_AISA / MS_AISA_BackEnd → Module ③ README 에 "강사 제공 참고 자료, 본인 저작 아님" 명시.

### E. 검증

- `ls` 로 `modules/0{1..6}/README.md` 6개 존재 확인
- README 내 참조 경로 22건 `ls` 일괄 확인 전량 OK
- `git diff --cached | grep -iE 'password|secret|key|token|bearer|subscription'` → 모두 섹션 헤더("Key Topics") 또는 설명문("keys are not committed", "subscription was decommissioned"), 실제 시크릿 값 0건

## 에러·미완료

- **Markdownlint 경고(MD060, MD024)**: 기존 README 에서도 있던 스타일 경고(table pipe 공백, 다국어 중복 헤딩). handoff traps 에 "현 상태 유지" 로 기록된 사항이라 무시.
- **미완료**: Highlights 2건 독립 README(재현 가이드 포함), 저작범위 3블록 Eric 직접 작성, SOHOBI URL 확정, Module ④ VM/Linux 자료 보강 여부 결정.

## 주의·회귀 위험

- **`modules/` 는 논리 인덱스**: 물리 재배치를 하지 않았으므로 `git log --follow` 로 개별 파일 히스토리 추적 가능. 추후 물리 재배치 결정이 난다면 `modules/0N/README.md` 의 상대 경로 전량을 함께 갱신해야 함.
- **경계 모호 디렉토리의 재분류 위험**: `1103_pyWebcrawl` 을 ②로 판정한 근거는 주제(크롤링). 추후 ①로 이동시키려면 Module ① README 표에 추가 + Module ② README 표에서 제거 필요.
- **강사 제공 자료(`C03_Newweb/Reference/MS_AISA*`)**: Module ③ README 에 명시는 했으나 **루트 README 저작범위 블록(③ 강사 제공 코드)** 에 TODO 로 남아 있음. 공개 전환 전 저작범위 완성 필수.
- **백업 bare clone** (`/Users/eric.j.park/Documents/GitHub/MS_SAY_EJP-backup-20260420-185548.git`): Content 단계 전체(Highlights 독립 README까지) 완료 후 사용자 승인 시 삭제.
- **원안 대비 절충안 선택**: 원안(물리 재배치) 의 "진입점 단일화" 목적은 달성했으나, 독자가 `C01_python/` 등 레거시 디렉토리를 직접 탐색할 여지가 남아 있음. 필요 시 각 `C0*/README.md` stub 을 추가해 `modules/0N/` 로 유도하는 방안 고려 가능.

## 이전 handoff 의 `unresolved` 재판정

| 원 항목 | 판정 | 근거 |
|---|---|---|
| HIGH (carry:1): `modules/01~06` 디렉토리 신설 + `git mv` 재배치 | **INVALIDATED** | C안 채택으로 물리 재배치 전제 무너짐. 논리 인덱스(`modules/0N/README.md`) 로 진입점 단일화 목적 달성 |
| HIGH (carry:1): 6개 모듈별 README(KO+EN) 초안 | **CLOSED** | 본 세션 `c4ea683` 로 완료. 6개 파일 모두 KO+EN 병기, 포함 디렉토리 표·핵심 주제·재현 주의 섹션 |
| HIGH (carry:1): Highlights 2건 독립 README | **carried (carry:2)** | 본 세션 미수행. 다음 세션 1순위 |
| MED (carry:1): 모듈 ④ Azure 인프라 산출물 공백 | **carried (carry:2)** | `modules/04/README.md` stub 에 "교재 학습, 코드 미공개" 명시는 했으나 VM/Linux 자료 보강 여부는 여전히 사용자 결정 대기 |
| LOW (carry:1): 저작범위 3블록 Eric 직접 작성 + 영문 README 검수 | **carried (carry:2)** | 루트 README TODO 마커 그대로, 사용자 작성 필요 |
| LOW: SOHOBI URL 미정 | **carried (carry:1)** | 사용자 응답 대기 |

## 다음 세션 (Phase 2 Content Step C 후보)

1. Highlights 2건 독립 README + 재현 가이드
   - Azure AI Integration Suite (`C04_AI/Feb03~Feb05` 통합 흐름)
   - Seoul Air Quality MVC (`C01_python/1110_pyOOP_mvc_airquality`)
2. 저작범위 3블록 Eric 직접 작성 요청·반영 (루트 README KO/EN 양쪽)
3. SOHOBI URL 사용자 확정 → 루트 README 갱신
4. Module ④ VM/Linux 자료 보강 여부 결정
5. (선택) 각 `C0*/README.md` stub 으로 `modules/0N/` 유도
6. 체크포인트 C 검수 → `gh repo edit --visibility public` (사용자 직접)

---

<!-- CLAUDE_HANDOFF_START -->
```yaml
branch: main
pr: null
prev: 2026-04-21-academy-phase2-content-stepA-handoff.md

unresolved:
  - HIGH (carry:2): Highlights 2건 독립 README — Azure AI Integration Suite(C04_AI/Feb03~05), Seoul Air Quality MVC(C01_python/1110_pyOOP_mvc_airquality). 재현 가이드 포함
  - MED (carry:2): 모듈 ④ Azure 인프라 VM/Linux 자료 보강 여부 — modules/04/README.md 는 stub 상태(교재 학습 명시), 노트/스크린샷 추가 여부 사용자 결정
  - LOW (carry:2): 저작범위 3블록 Eric 직접 작성 + 영문 README 검수 — 루트 README KO/EN 양쪽 TODO 마커
  - LOW (carry:1): SOHOBI URL 미정 — 사용자 확정 후 루트 README KO/EN 양쪽 placeholder 교체

decisions:
  - 논리 인덱스 채택: modules/0N/README.md 는 C01~C04 서브디렉토리를 가리키는 상대경로 인덱스. 물리 재배치 없음 — git log --follow 로 히스토리 추적 가능
  - 모듈 경계 판정: 1103_pyWebcrawl 은 Module ②(주제: 크롤링), Module ① 에서 제외. Jan22_Backup/Jan23_Backup 은 Module ⑤(텍스트/이미지 처리), Jan26_ML 은 Module ⑤(고전 ML), Jan27~30 은 Module ⑤(딥러닝 이론·TF), Feb03~05 는 Module ⑥(Azure AI)
  - 모듈 ③ 포함 범위: C02_web/ 의 1117/1119/1120/1124~1127/dec08~dec10 + C03_Newweb/ 전체. Reference/MS_AISA* 는 강사 제공 자료로 명시
  - CLOSED: 6개 모듈별 README(KO+EN) — 본 세션 c4ea683 로 완료
  - CLOSED: 루트 README 모듈 표 링크를 modules/0N/ 로 교체 — KO/EN 양쪽
  - INVALIDATED: modules/01~06 물리 재배치(git mv) — C안 채택으로 전제 무너짐. 진입점 단일화 목적은 논리 인덱스로 달성

next:
  1. Highlights 2건 독립 README + 재현 가이드 (Azure AI Integration Suite, Seoul Air Quality MVC)
  2. 저작범위 3블록 Eric 작성 요청·반영
  3. SOHOBI URL 확정·갱신
  4. Module ④ 자료 보강 여부 결정
  5. (선택) 각 C0*/README.md stub 으로 modules/0N/ 유도
  6. 체크포인트 C 검수
  7. gh repo edit --visibility public (사용자 직접)

traps:
  - modules/0N/README.md 의 참조 경로는 ../../C0*/... 형태의 상대 경로. C0* 디렉토리 이동·삭제 시 전량 깨짐
  - Module 경계가 모호한 디렉토리(1103_pyWebcrawl, Jan22/23_Backup, PIVOT, Reference)는 본 세션 판정 근거에 맞춰 재분류 가능 — 변경 시 관련 모듈 README 2개(원 모듈·새 모듈) 동시 수정
  - Markdownlint MD049/MD060/MD024 경고는 스타일 preference, GitHub 렌더 영향 없음 — 현 상태 유지
  - Highlights 2건 독립 README 는 재현 가이드 포함 필수 — .env 키 리스트, 리소스 생성 순서, 예상 출력 포함
  - 강사 제공 자료(C03_Newweb/Reference/MS_AISA*)는 Module ③ README 에 명시됨 — 루트 저작범위 블록 완성 전 공개 금지
  - 저작범위 3블록·SOHOBI URL·Module ④ 자료 보강 여부는 모두 사용자 응답 대기 — 임의 대필·추측 금지
  - 백업 bare clone `/Users/eric.j.park/Documents/GitHub/MS_SAY_EJP-backup-20260420-185548.git` 는 Content 단계 전체 완료 전 삭제 금지
  - 커밋 전 `git diff --cached | grep -iE 'password|secret|key|token|bearer|subscription'` 자동 점검 유지
```
<!-- CLAUDE_HANDOFF_END -->
