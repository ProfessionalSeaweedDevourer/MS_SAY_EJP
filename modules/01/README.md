# Module ① — AI Foundations (Python · SQL · MongoDB)

> **[🇰🇷 한국어](#-한국어)** · **[🇺🇸 English](#-english)**

---

## 🇰🇷 한국어

MS AI Academy 1기 커리큘럼의 출발점. Python 언어 기초 → OOP → DB 연결(Oracle/SQL, MongoDB) → MVC 패턴까지 **"코드로 데이터를 다루기 위한 공통 토대"** 를 쌓은 구간입니다.

### 🗂 포함 디렉토리 (2024-10 ~ 2024-11)

| 경로 | 주제 |
|---|---|
| [../../C01_python/1015_VSCode/](../../C01_python/1015_VSCode/) | VSCode · Python 환경 설정 |
| [../../C01_python/1016_pyVar/](../../C01_python/1016_pyVar/) | 변수·자료형 |
| [../../C01_python/1017_pyIO_calc/](../../C01_python/1017_pyIO_calc/) | I/O · 기본 연산 |
| [../../C01_python/1020_pyLogic_collection/](../../C01_python/1020_pyLogic_collection/) | 제어문 · 컬렉션 |
| [../../C01_python/1021_pyFunc_collection/](../../C01_python/1021_pyFunc_collection/) | 함수 · 컬렉션 심화 |
| [../../C01_python/1022_pyLogic_lambda/](../../C01_python/1022_pyLogic_lambda/) | 람다 · 고차함수 |
| [../../C01_python/1023_pyLogic_func/](../../C01_python/1023_pyLogic_func/) | 함수 스코프 · 재귀 |
| [../../C01_python/1024_pyFunc_games/](../../C01_python/1024_pyFunc_games/) | 함수 실습(게임) |
| [../../C01_python/1027_pyOOP_class_method/](../../C01_python/1027_pyOOP_class_method/) | 클래스 · 메서드 |
| [../../C01_python/1028_pyOOP_games/](../../C01_python/1028_pyOOP_games/) | OOP 실습(게임) |
| [../../C01_python/1029_pyOOP_module_relation/](../../C01_python/1029_pyOOP_module_relation/) | 모듈 · 상속·합성 |
| [../../C01_python/1030_pyPackage_str/](../../C01_python/1030_pyPackage_str/) | 패키지 · 문자열 처리 |
| [../../C01_python/1031_pyOOP_loop/](../../C01_python/1031_pyOOP_loop/) | OOP 반복문 응용 |
| [../../C01_python/1107_pyDBconn_fromnov03/](../../C01_python/1107_pyDBconn_fromnov03/) | Python ↔ Oracle/SQL 연결 |
| [../../C01_python/1110_pyOOP_mvc_airquality/](../../C01_python/1110_pyOOP_mvc_airquality/) | **MVC 패턴** — 서울 대기질 수집·적재 (⭐ Highlight) |
| [../../C01_python/1111_pyMVC_prac_webmall/](../../C01_python/1111_pyMVC_prac_webmall/) | MVC 실습(웹몰) |
| [../../C01_python/1112_pyMVC_expense/](../../C01_python/1112_pyMVC_expense/) | MVC 실습(가계부) |
| [../../C01_python/1114_pyMongoDB/](../../C01_python/1114_pyMongoDB/) | MongoDB 연동 |

> `1103_pyWebcrawl/` 은 시간순으로 이 모듈 사이에 위치하지만 주제상 **Module ② (데이터 수집)** 로 분류했습니다.

### 🎯 핵심 학습 주제

- Python 문법·자료구조·함수형 기법 (람다·map·filter·reduce)
- OOP 4대 원칙(캡슐화·상속·다형성·추상화)을 게임·카운터 예제로 내재화
- Oracle/SQL · MongoDB 드라이버를 통한 양방향 CRUD
- **MVC 패턴**으로 수집→파싱→적재→출력 파이프라인 구성

### ⭐ Highlight

**Seoul Air Quality MVC** — [../../C01_python/1110_pyOOP_mvc_airquality/](../../C01_python/1110_pyOOP_mvc_airquality/) 가 본 모듈의 대표 산출물입니다. 서울시 공공 API(XML) 수집 → 파싱 → Oracle 적재 → CSV 내보내기를 MVC 구조로 구현.

### 🔁 재현 주의

- Oracle 접속 계정·Wallet 파일은 저장소에 포함되지 않습니다. 본인 환경에서 `cx_Oracle` 접속 정보를 주입해야 합니다.
- MongoDB 는 로컬 기본 포트(27017) 기준으로 작성되었습니다.

---

## 🇺🇸 English

The entry point of the MS AI Academy curriculum. This module builds the shared foundation for "manipulating data with code" — Python basics → OOP → database connectivity (Oracle/SQL, MongoDB) → MVC pattern.

### 🗂 Included Directories (Oct–Nov 2024)

| Path | Topic |
|---|---|
| [../../C01_python/1015_VSCode/](../../C01_python/1015_VSCode/) | VSCode · Python setup |
| [../../C01_python/1016_pyVar/](../../C01_python/1016_pyVar/) | Variables · types |
| [../../C01_python/1017_pyIO_calc/](../../C01_python/1017_pyIO_calc/) | I/O · basic arithmetic |
| [../../C01_python/1020_pyLogic_collection/](../../C01_python/1020_pyLogic_collection/) | Control flow · collections |
| [../../C01_python/1021_pyFunc_collection/](../../C01_python/1021_pyFunc_collection/) | Functions · advanced collections |
| [../../C01_python/1022_pyLogic_lambda/](../../C01_python/1022_pyLogic_lambda/) | Lambda · higher-order functions |
| [../../C01_python/1023_pyLogic_func/](../../C01_python/1023_pyLogic_func/) | Scope · recursion |
| [../../C01_python/1024_pyFunc_games/](../../C01_python/1024_pyFunc_games/) | Function practice (games) |
| [../../C01_python/1027_pyOOP_class_method/](../../C01_python/1027_pyOOP_class_method/) | Classes · methods |
| [../../C01_python/1028_pyOOP_games/](../../C01_python/1028_pyOOP_games/) | OOP practice (games) |
| [../../C01_python/1029_pyOOP_module_relation/](../../C01_python/1029_pyOOP_module_relation/) | Modules · inheritance/composition |
| [../../C01_python/1030_pyPackage_str/](../../C01_python/1030_pyPackage_str/) | Packages · string processing |
| [../../C01_python/1031_pyOOP_loop/](../../C01_python/1031_pyOOP_loop/) | OOP loop applications |
| [../../C01_python/1107_pyDBconn_fromnov03/](../../C01_python/1107_pyDBconn_fromnov03/) | Python ↔ Oracle/SQL |
| [../../C01_python/1110_pyOOP_mvc_airquality/](../../C01_python/1110_pyOOP_mvc_airquality/) | **MVC pattern** — Seoul air quality ingest (⭐ Highlight) |
| [../../C01_python/1111_pyMVC_prac_webmall/](../../C01_python/1111_pyMVC_prac_webmall/) | MVC practice (web mall) |
| [../../C01_python/1112_pyMVC_expense/](../../C01_python/1112_pyMVC_expense/) | MVC practice (expense tracker) |
| [../../C01_python/1114_pyMongoDB/](../../C01_python/1114_pyMongoDB/) | MongoDB integration |

> `1103_pyWebcrawl/` sits chronologically inside this window, but is classified under **Module ② (Data Ingestion)** by topic.

### 🎯 Key Topics

- Python syntax, data structures, functional idioms (lambda · map · filter · reduce)
- OOP (encapsulation · inheritance · polymorphism · abstraction) through game/counter exercises
- Bidirectional CRUD against Oracle/SQL and MongoDB drivers
- **MVC pattern** pipelines: ingest → parse → persist → export

### ⭐ Highlight

**Seoul Air Quality MVC** — [../../C01_python/1110_pyOOP_mvc_airquality/](../../C01_python/1110_pyOOP_mvc_airquality/) is the module's flagship deliverable. Seoul public-API (XML) ingest → parse → Oracle persist → CSV export, structured as MVC.

### 🔁 Reproduction Notes

- Oracle credentials/Wallet files are not committed. Supply your own `cx_Oracle` connection info.
- MongoDB assumes the default local port (27017).
