# 2026-04-21 Academy 리포 Phase 2 Content Step C — Highlights 2건 독립 README 세션 인수인계

## 세션 개요

Phase 2 Content Step C 를 `main` 에 단일 커밋(`126abf7`)으로 반영. Step B handoff 의 `unresolved` 1순위였던 HIGH (carry:2) "Highlights 2건 독립 README" 를 완료. Azure AI Integration Suite (C04_AI Feb03~05 통합) 와 Seoul Air Quality MVC (C01_python 1110) 에 각각 KO+EN 병기 README 를 배치하고 재현 가이드(리소스 생성 순서·환경변수·DDL·실행 순서·예상 출력) 포함. modules/01 · modules/06 의 Highlight 섹션에서 신규 README 로 역링크 추가.

## 브랜치·커밋 상태

- **브랜치**: `main` (clean)
- **이전 HEAD**: `f5103b8` (Step B handoff 문서)
- **본 세션 커밋**: `126abf7 docs: add Highlight READMEs — Azure AI Integration Suite & Seoul Air Quality MVC`
- **원격**: 미푸시 상태 (본 handoff 커밋과 함께 push 예정)

## 수행 작업 요약

### A. Highlight A — Azure AI Integration Suite

- 위치: `C04_AI/README.md` 신규 (163줄)
- 원안 "Feb03_AzureAI/README.md · Feb04_azureAI/README.md · Feb05_Azure_Language/README.md 3개 분산" 대신 **C04_AI 루트 단일 README 통합** 채택 — 사유: 사용자가 "학습 진행 내용이 다소 빈약한 날도 있어 내용 중심 합치기가 합리적" 이라고 확인
- 범위: Feb03~05 9개 스크립트를 서비스/SDK/기능 매핑표로 정리. 1월분 딥러닝(Jan27~30) 은 Module ⑤ 로 명시 위임
- 재현 가이드: 6단계 리소스 생성 순서 → `.env` 키 리스트(기존 `.env.example` 재활용) → Python 패키지 설치 명령 → 9단계 실행 순서표(파일/입력/예상 출력)
- 개별 파일 이슈 명시: `2_dalle.py` 는 상단 import/client 초기화 제거된 상태, `1_azurevision_ocr_webimg.py` 는 `from time import sleep` 누락

### B. Highlight B — Seoul Air Quality MVC

- 위치: `C01_python/1110_pyOOP_mvc_airquality/README.md` 신규 (299줄)
- 13개 파일을 3개 섹션(데이터 파이프라인 / MVC 미니앱 / OOP 기초)으로 재구성. 같은 디렉토리 안에 성격이 다른 3흐름이 공존하는 구조를 명시
- DDL 3종(`SEOUL_AIR_QUALITY`, `OWMW`, `회사`) 명시 — `SeoulAirQuality_Parser.py` 는 drop/create 포함, 나머지 2개는 사전 생성 전제
- 커넥션 교체: 교실 LAN IP(`195.168.9.{207,249,71}`) + 기본 계정(`ericjpark/0000`) 을 파일:라인 단위로 지목
- 알려진 버그 명시: `AirQualityDB.py` close 순서 버그, `OWMtoCSV.py` 미정의 변수(`data`), `1110_2_AOP.py` AOP 섹션 미완

### C. 시크릿 재노출 방지

- 초안에서 Seoul API 키(32-hex)·OWM API 키(32-hex) 를 README 본문에 리터럴로 포함 → 기존 소스에는 이미 하드코딩되어 있으나 README 재게시는 노출면 확대로 판단, 리터럴 제거 후 "URL 경로 내 키 부분 교체" · "`appid=...` 값 교체" 로 지시화
- 교실 LAN IP(`195.168.9.x`) 와 비밀번호 `0000` 은 유지: 외부 비라우팅 대역 + Oracle XE 학습 기본값 + 경고 문구 동반

### D. 역링크

- `modules/01/README.md` Highlight 섹션 KO/EN 양쪽에 "재현 가이드는 [1110 README] 참고" 문장 추가
- `modules/06/README.md` Highlight 섹션(KO) 에 "리소스 생성 순서·환경변수·실행 순서·예상 출력은 [C04_AI/README] 참고" 추가 (EN 섹션은 미편집 — 차회 작업 가능)

### E. 검증

- 생성된 README 내 상대경로 22건 중 핵심 파일 실재 확인 (Feb03~05 9개, 1110 13개, `.env.example`, `modules/01,06/README.md`)
- `git diff --cached | grep -iE '575a4655|baff8f3c'` → 0건 (API 키 리터럴 제거 확인)
- 커밋 후 `git status` clean

## 에러·미완료

- **Markdownlint MD060/MD024**: Step B 이래 기존 경고 유지. handoff traps 에 "현 상태 유지" 명시된 바 무시.
- **modules/06/README.md EN Highlight 섹션 미편집**: KO 만 업데이트. 영문 검수(carry:3) 시점에 같이 처리 예정.

## 주의·회귀 위험

- **API 키 원본 보존 vs 재게시 금지**: 소스 파일(`SeoulAirQuality_Parser.py` 등)에는 여전히 실제 Seoul/OWM 키가 하드코딩됨. 현재는 README 에서 중복 게시만 방지 상태. 추후 공개 전환 시 소스 자체의 env-var 전환 또는 키 플레이스홀더화 검토 필요.
- **Highlight README 내 경로**: `C04_AI/README.md` 는 `Feb03_AzureAI/1_gpt.py` 같은 **상대 경로**만 사용. `C04_AI/` 자체가 이동/개명되면 내부 링크는 유지되나 `modules/06` 에서의 역링크가 깨짐.
- **`1110_pyOOP_mvc_airquality/README.md` 의 DDL 재현성**: `SEOUL_AIR_QUALITY` 는 스크립트가 drop/create 하나 `OWMW` / `회사` 는 사용자가 수동 생성해야 함. 재현 시도자가 이 구분을 놓치면 `ORA-00942: table or view does not exist` 발생.
- **본 세션 원격 미푸시**: handoff 커밋과 함께 이번에 푸시 예정. Step B handoff 는 이미 푸시됨(`f5103b8`).

## 이전 handoff 의 `unresolved` 재판정

| 원 항목 | 판정 | 근거 |
|---|---|---|
| HIGH (carry:2): Highlights 2건 독립 README | **CLOSED** | 본 세션 `126abf7` 로 완료. Azure AI Integration Suite · Seoul Air Quality MVC 모두 KO+EN 병기, 재현 가이드(리소스 생성·env·DDL·실행·예상 출력) 포함 |
| MED (carry:2): 모듈 ④ Azure 인프라 VM/Linux 자료 보강 여부 | **carried (carry:3)** | 사용자 결정 대기 중. carry:3 도달 — 본 저장소의 공개 목적(코드·학습 기록) 상 VM/스크린샷은 선택사항이며, 보강 없이도 `modules/04/README.md` stub 으로 "교재 학습" 명시되어 있으므로 **다음 세션에서 closure 여부 적극 검토** 필요 |
| LOW (carry:2): 저작범위 3블록 Eric 작성 + 영문 README 검수 | **carried (carry:3)** | 사용자 직접 작성 대기. carry:3 도달 — Eric 외 대필 금지 원칙상 자동 closure 불가. 공개 전환 직전 단일 과제로 묶어 처리 권장 |
| LOW (carry:1): SOHOBI URL 미정 | **carried (carry:2)** | 사용자 응답 대기. URL 확정 시 KO/EN 양쪽 placeholder 1회 교체 |

## 다음 세션 후보 (Phase 2 Content Step D 또는 Pre-Publish)

1. 저작범위 3블록(③ 강사 제공 코드, ④ 교재 학습, 기타) Eric 직접 작성 요청 → 루트 README KO/EN 양쪽 반영
2. SOHOBI URL 확정 → 루트 README KO/EN 양쪽 placeholder 교체
3. Module ④ VM/Linux 자료 보강 여부 결정 (보강 OR closure)
4. `modules/06/README.md` EN Highlight 섹션에 `C04_AI/README.md` 역링크 추가 (KO 만 업데이트됨)
5. (선택) 소스 파일의 실제 API 키(Seoul/OWM) env-var 전환 또는 플레이스홀더화
6. (선택) 각 `C0*/README.md` stub 으로 `modules/0N/` 유도
7. 체크포인트 C 검수 → `gh repo edit --visibility public` (사용자 직접)
8. (공개 후) 백업 bare clone (`MS_SAY_EJP-backup-20260420-185548.git`) 삭제

---

<!-- CLAUDE_HANDOFF_START -->
```yaml
branch: main
pr: null
prev: 2026-04-21-academy-phase2-content-stepB-handoff.md

unresolved:
  - MED (carry:3): 모듈 ④ Azure 인프라 VM/Linux 자료 보강 여부 — modules/04/README.md 는 stub("교재 학습") 상태. carry:3 도달 — 다음 세션에서 보강 OR closure 적극 결정
  - LOW (carry:3): 저작범위 3블록 Eric 직접 작성 + 영문 README 검수 — 루트 README KO/EN TODO 마커. carry:3 도달 — Eric 대필 금지라 자동 closure 불가, 공개 직전 단일 과제로 묶어 처리
  - LOW (carry:2): SOHOBI URL 미정 — 사용자 확정 후 루트 README KO/EN 양쪽 placeholder 교체
  - LOW (carry:1): modules/06/README.md EN Highlight 섹션에 C04_AI/README.md 역링크 추가 — 본 세션 KO 만 업데이트됨

decisions:
  - C04_AI Highlight 는 Feb03~05 3일치를 C04_AI/README.md 단일로 통합. 사유: 일자별 실습 분량 편차로 3개 분산 README 보다 통합이 합리적(사용자 확인)
  - API 키 리터럴(Seoul/OWM 32-hex)은 README 에서 제거하되 소스 파일의 하드코딩은 유지. 사유: 학습 기록 원본 보존 + README 재게시로 인한 노출면 확대 방지. 단 공개 전환 시 소스 env-var 전환 재검토 대상
  - 교실 LAN IP(195.168.9.x)와 Oracle XE 기본 패스워드(0000)는 README 에 명시 보존. 사유: 외부 비라우팅 대역 + 학습 기본값이라 실질 유출 위험 없음, 오히려 재현 시 교체 지점 명확화에 기여
  - CLOSED: Highlights 2건 독립 README — 본 세션 126abf7 로 완료. C04_AI/README.md + C01_python/1110_pyOOP_mvc_airquality/README.md, 둘 다 KO+EN 병기 및 재현 가이드 포함

next:
  1. 저작범위 3블록 Eric 작성 요청·반영 (루트 README KO/EN)
  2. SOHOBI URL 확정·갱신
  3. Module ④ 자료 보강 여부 결정 (보강 OR closure)
  4. modules/06/README.md EN Highlight 역링크 추가
  5. (선택) 소스 API 키 env-var 전환
  6. (선택) 각 C0*/README.md stub 으로 modules/0N/ 유도
  7. 체크포인트 C 검수
  8. gh repo edit --visibility public (사용자 직접)

traps:
  - Highlight README 내 상대경로는 `C04_AI/Feb03_AzureAI/...` 와 `C01_python/1110_pyOOP_mvc_airquality/...` 형태. 상위 디렉토리 개명/이동 시 modules/01·06 의 역링크가 깨짐
  - 소스 파일에는 여전히 Seoul/OWM API 키가 하드코딩 — README 에서만 제거됨. 공개 전 키 플레이스홀더화 또는 env-var 전환 검토
  - `1110_pyOOP_mvc_airquality/README.md` DDL 섹션: SEOUL_AIR_QUALITY 는 스크립트가 drop/create, OWMW·회사 는 사용자가 수동 생성 필요 — 혼동 시 ORA-00942
  - modules/06/README.md EN 섹션 Highlight 역링크 미추가 (KO 만) — 다음 세션 반드시 반영
  - Markdownlint MD060/MD024 경고는 스타일 preference, GitHub 렌더 영향 없음 — 현 상태 유지
  - 저작범위 3블록·SOHOBI URL·Module ④ 자료 보강은 모두 사용자 응답 대기 — 임의 대필·추측 금지
  - 백업 bare clone `/Users/eric.j.park/Documents/GitHub/MS_SAY_EJP-backup-20260420-185548.git` 는 Content 단계 전체(공개 전환 포함) 완료 전 삭제 금지
  - 커밋 전 `git diff --cached | grep -iE 'password|secret|key|token|bearer|subscription'` 자동 점검 유지. 본 세션에서는 API 키 32-hex 리터럴도 추가 확인(`575a4655|baff8f3c`)
```
<!-- CLAUDE_HANDOFF_END -->
