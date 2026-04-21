# Highlight — Seoul Air Quality MVC (1110_pyOOP_mvc_airquality)

> **[🇰🇷 한국어](#-한국어)** · **[🇺🇸 English](#-english)**

Python OOP 수업의 통합 산출물(Highlight). 공공 API(서울 열린데이터광장 실시간 대기질 · OpenWeatherMap) 호출 → XML/JSON 파싱 → Oracle DB 적재 → CSV 중복 제거 내보내기까지 하나의 파이프라인으로 묶고, 별도로 MVC 구조(Controller / View / DAO / Entity) 를 통한 "회사 등록" 미니 프로그램을 두어 OOP 개념 전체를 한 폴더에 응축했습니다.

---

## 🇰🇷 한국어

### 🎯 학습 목표

- `http.client` 로 외부 API 호출, `xml.etree.ElementTree` / `json` 으로 응답 파싱
- `oracledb` 로 Oracle DB 연결·테이블 DDL·`executemany` 대량 삽입·예외 처리
- `pandas` 로 CSV 중복 제거(복합 키 `측정일시` + `측정소명`) 와 증분 append
- OOP 기초(클래스·인스턴스·메서드) 와 MVC 역할 분리(`View → Controller → DAO → DB`)
- 공통 자원(`DBManager`) 을 **staticmethod** 로 추출해 커넥션/커서 수명 일관화

### 🗂 파일 구성

#### 데이터 파이프라인 (End-to-end)

| 파일 | 역할 |
|---|---|
| [SeoulAirQuality_Parser.py](SeoulAirQuality_Parser.py) | **메인 파이프라인** — 서울 대기질 API → XML 파싱 → `SEOUL_AIR_QUALITY` 테이블 drop·create·bulk insert → CSV 증분 저장 |
| [Parse_SeoulAirQuality.bat](Parse_SeoulAirQuality.bat) | 위 스크립트를 Windows 스케줄러로 돌릴 수 있도록 한 배치 실행 파일 |
| [OWM_Parser.py](OWM_Parser.py) | OpenWeatherMap API → JSON 파싱 → `OWMW` 테이블 INSERT (분리 실습) |
| [OWMtoCSV.py](OWMtoCSV.py) | `OWMW` 테이블 → CSV 내보내기 (⚠️ 미완 · 주의 참고) |
| [AirQualityDB.py](AirQualityDB.py) | 위 통합 파서 이전 단계의 원시 구현 (⚠️ close 순서 버그 · 학습 기록 원본 보존) |

#### MVC 구조 미니 애플리케이션 (회사 등록)

| 파일 | 레이어 |
|---|---|
| [homeController.py](homeController.py) | Controller — 진입점, View 호출 → DAO 호출 → View 결과 출력 |
| [consoleScreen.py](consoleScreen.py) | View — 사용자 입력 수집, 결과 출력 (정적 메서드) |
| [companyDAO.py](companyDAO.py) | DAO — `INSERT INTO 회사` SQL 실행, rowcount 로 성공 판정 |
| [company.py](company.py) | Entity — `Company(name, addr, ceo, emp)` 값 객체 |
| [ejp/ejpDBManager.py](ejp/ejpDBManager.py) | 공통 인프라 — `makeConCur` / `closeConCur` staticmethod 로 연결 수명 일원화 |

#### OOP 기초

| 파일 | 주제 |
|---|---|
| [1110_1_select.py](1110_1_select.py) | OOP 도입 전 단순 SELECT (평균 가격 조회) |
| [1110_2_AOP.py](1110_2_AOP.py) | `Human` 클래스로 OOP 기본기. (AOP 섹션은 수업 중단되어 미완) |

### 🔁 재현 가이드

#### 1. 전제

- **Python 3.10+** · `pip install oracledb pandas`
- **Oracle Database** (XE 11g / 21c 권장). Thin mode(`oracledb`) 는 Oracle Client 불필요.
- **서울 열린데이터광장** (`data.seoul.go.kr`) 계정에서 `RealtimeCityAir` 서비스 API 키 발급
- **OpenWeatherMap** (`openweathermap.org`) 무료 API 키 발급

#### 2. DB 스키마 (자동 생성)

`SeoulAirQuality_Parser.py` 는 실행 시 아래 테이블을 **drop → create** 합니다:

```sql
CREATE TABLE SEOUL_AIR_QUALITY (
    saq_date     VARCHAR2(20) NOT NULL,
    saq_area     VARCHAR2(50),
    saq_district VARCHAR2(50) NOT NULL,
    saq_pm10     NUMBER(10, 2),
    saq_pm25     NUMBER(10, 2),
    saq_score    VARCHAR2(10),
    CONSTRAINT PK_SEOUL_AIR_QUALITY PRIMARY KEY (saq_date, saq_district)
);
```

`OWM_Parser.py` 는 사전에 다음 테이블이 존재한다고 가정합니다 (수업에서 사전 생성):

```sql
CREATE TABLE OWMW (
    w_date DATE,
    w_desc VARCHAR2(200),
    w_temp NUMBER(5,2),
    w_humi NUMBER(3)
);
```

MVC 샘플 (`homeController.py`) 은 다음 테이블을 필요로 합니다:

```sql
CREATE TABLE 회사 (
    name VARCHAR2(100),
    addr VARCHAR2(200),
    ceo  VARCHAR2(100),
    emp  NUMBER(10)
);
```

#### 3. 커넥션 문자열 교체 (필수)

원본 파일들에는 **수업 교실 LAN IP (`195.168.9.x`)** 와 기본 계정(`ericjpark/0000`) 이 하드코딩되어 있습니다. 아래 파일의 connect 문자열을 본인 환경으로 교체해야 합니다:

- `SeoulAirQuality_Parser.py:59` — `ericjpark/0000@195.168.9.207:1521/xe`
- `OWM_Parser.py:39`, `OWMtoCSV.py:6`, `AirQualityDB.py:12` — `...@195.168.9.249:1521/xe`
- `companyDAO.py:5` — `...@195.168.9.71:1521/xe`

권장 형식: `사용자명/비밀번호@호스트:1521/서비스명`. 예: `hr/hrpwd@localhost:1521/XEPDB1`.

#### 4. API 키 설정 (필수)

각 파일은 환경변수에서 키를 읽습니다. 실행 전 본인 키를 `.env` 또는 셸 환경변수로 설정하십시오.

- `SEOUL_API_KEY` — [서울 열린데이터광장](https://data.seoul.go.kr/) 에서 발급. `SeoulAirQuality_Parser.py`, `AirQualityDB.py` 에서 사용
- `OWM_API_KEY` — [OpenWeatherMap](https://home.openweathermap.org/api_keys) 에서 발급. `OWM_Parser.py` 에서 사용

> 저장소 루트 `.env.example` 에 두 변수가 정의되어 있으니, `.env` 로 복사 후 값만 채워 넣으면 됩니다.

#### 5. 실행

```
# 1) 대기질 파이프라인 (API → DB → CSV)
python SeoulAirQuality_Parser.py

# 2) (선택) 날씨 저장
python OWM_Parser.py

# 3) MVC 회사 등록 데모
python homeController.py
```

#### 6. 예상 출력 (대기질 파이프라인 성공 시)

```
기존 테이블 SEOUL_AIR_QUALITY 삭제 완료.
새 테이블 SEOUL_AIR_QUALITY 생성 완료.

✅ DB 삽입 완료: 총 25개 레코드가 삽입되었습니다.

--- CSV 저장 완료 ---
'seoul_air_quality_data.csv' 파일에 25개의 신규 레코드를 추가했습니다.
```

회사 등록 데모:

```
회사명: 아크로보스
주소: Lordran
사장: Gwyn
직원 수: 4
등록 성공.
```

### ⚠️ 주의

- **AirQualityDB.py** 는 루프 안에서 `con.close()` 를 호출해 2회차에서 실패합니다. 수업에서 통합 버전(`SeoulAirQuality_Parser.py`) 으로 개선된 원본을 그대로 보존한 상태.
- **OWMtoCSV.py** 는 `f.write(data)` 의 `data` 가 정의되지 않은 상태로 커밋되어 그대로는 실행되지 않습니다 (`date` 변수를 쓸 의도였던 것으로 보임). 학습 기록 보존 의도로 원본 유지.
- **1110_2_AOP.py** 의 AOP 섹션은 수업 시간이 부족해 주석만 남았습니다 — OOP 파트까지만 동작.
- `195.168.9.x` 대역은 교실 LAN 으로, 외부에서 라우팅되지 않습니다. 패스워드 `0000` 은 Oracle XE 수업 기본값입니다.

---

## 🇺🇸 English

### 🎯 Learning Objectives

- Call external APIs with `http.client`; parse responses with `xml.etree.ElementTree` / `json`
- Use `oracledb` for Oracle connections, table DDL, `executemany` bulk insert, and exception handling
- Deduplicate CSV output with `pandas` (composite key `측정일시` + `측정소명`) and append incrementally
- OOP basics (class / instance / method) and MVC separation (`View → Controller → DAO → DB`)
- Extract shared resources (`DBManager`) as **staticmethod**s to make connection/cursor lifecycles consistent

### 🗂 File Layout

#### Data pipeline (end-to-end)

| File | Role |
|---|---|
| [SeoulAirQuality_Parser.py](SeoulAirQuality_Parser.py) | **Main pipeline** — Seoul Air Quality API → XML parse → drop / create / bulk insert into `SEOUL_AIR_QUALITY` → incremental CSV write |
| [Parse_SeoulAirQuality.bat](Parse_SeoulAirQuality.bat) | Batch wrapper so the pipeline can be scheduled on Windows |
| [OWM_Parser.py](OWM_Parser.py) | OpenWeatherMap API → JSON parse → INSERT into `OWMW` |
| [OWMtoCSV.py](OWMtoCSV.py) | `OWMW` table → CSV export (⚠️ incomplete — see notes) |
| [AirQualityDB.py](AirQualityDB.py) | Pre-integration raw implementation (⚠️ close-order bug; kept as-is for learning record) |

#### MVC mini-application (Company registration)

| File | Layer |
|---|---|
| [homeController.py](homeController.py) | Controller — entrypoint, orchestrates View → DAO → View |
| [consoleScreen.py](consoleScreen.py) | View — collects input, prints result (static methods) |
| [companyDAO.py](companyDAO.py) | DAO — runs `INSERT INTO 회사`, uses `cur.rowcount` to decide success |
| [company.py](company.py) | Entity — `Company(name, addr, ceo, emp)` value object |
| [ejp/ejpDBManager.py](ejp/ejpDBManager.py) | Shared infra — `makeConCur` / `closeConCur` staticmethods |

#### OOP basics

| File | Topic |
|---|---|
| [1110_1_select.py](1110_1_select.py) | Plain SELECT (avg product price) before OOP |
| [1110_2_AOP.py](1110_2_AOP.py) | `Human` class for OOP basics. (AOP section left unfinished — class time ran out) |

### 🔁 Reproduction Guide

#### 1. Prerequisites

- **Python 3.10+** · `pip install oracledb pandas`
- **Oracle Database** (XE 11g / 21c recommended). `oracledb` thin mode needs no Oracle Client install.
- **Seoul Open Data Plaza** (`data.seoul.go.kr`) API key for `RealtimeCityAir`
- **OpenWeatherMap** (`openweathermap.org`) free API key

#### 2. DB schema (auto-managed where possible)

`SeoulAirQuality_Parser.py` **drops and recreates** this table on each run:

```sql
CREATE TABLE SEOUL_AIR_QUALITY (
    saq_date     VARCHAR2(20) NOT NULL,
    saq_area     VARCHAR2(50),
    saq_district VARCHAR2(50) NOT NULL,
    saq_pm10     NUMBER(10, 2),
    saq_pm25     NUMBER(10, 2),
    saq_score    VARCHAR2(10),
    CONSTRAINT PK_SEOUL_AIR_QUALITY PRIMARY KEY (saq_date, saq_district)
);
```

`OWM_Parser.py` assumes this table already exists (the class pre-created it):

```sql
CREATE TABLE OWMW (
    w_date DATE,
    w_desc VARCHAR2(200),
    w_temp NUMBER(5,2),
    w_humi NUMBER(3)
);
```

The MVC sample (`homeController.py`) needs:

```sql
CREATE TABLE 회사 (
    name VARCHAR2(100),
    addr VARCHAR2(200),
    ceo  VARCHAR2(100),
    emp  NUMBER(10)
);
```

#### 3. Replace connection strings (required)

The source files hardcode the **classroom LAN IPs (`195.168.9.x`)** and the default account (`ericjpark/0000`). Replace them in:

- `SeoulAirQuality_Parser.py:59` — `ericjpark/0000@195.168.9.207:1521/xe`
- `OWM_Parser.py:39`, `OWMtoCSV.py:6`, `AirQualityDB.py:12` — `...@195.168.9.249:1521/xe`
- `companyDAO.py:5` — `...@195.168.9.71:1521/xe`

Recommended format: `user/password@host:1521/service`. Example: `hr/hrpwd@localhost:1521/XEPDB1`.

#### 4. Configure API keys (required)

Each script reads its key from environment variables. Set your own values in `.env` (or your shell) before running.

- `SEOUL_API_KEY` — issue at [Seoul Open Data Plaza](https://data.seoul.go.kr/). Used by `SeoulAirQuality_Parser.py` and `AirQualityDB.py`.
- `OWM_API_KEY` — issue at [OpenWeatherMap](https://home.openweathermap.org/api_keys). Used by `OWM_Parser.py`.

> Both variables are declared in the repo-root `.env.example`; copy it to `.env` and fill in the values.

#### 5. Run

```
# 1) Air-quality pipeline (API → DB → CSV)
python SeoulAirQuality_Parser.py

# 2) (optional) Weather insert
python OWM_Parser.py

# 3) MVC company-registration demo
python homeController.py
```

#### 6. Expected output (successful air-quality run)

```
기존 테이블 SEOUL_AIR_QUALITY 삭제 완료.
새 테이블 SEOUL_AIR_QUALITY 생성 완료.

✅ DB 삽입 완료: 총 25개 레코드가 삽입되었습니다.

--- CSV 저장 완료 ---
'seoul_air_quality_data.csv' 파일에 25개의 신규 레코드를 추가했습니다.
```

Company registration demo:

```
회사명: Acroboss
주소: Lordran
사장: Gwyn
직원 수: 4
등록 성공.
```

### ⚠️ Notes

- **AirQualityDB.py** calls `con.close()` inside the loop, so the second iteration fails. Kept as-is because the integrated rewrite (`SeoulAirQuality_Parser.py`) is the canonical version.
- **OWMtoCSV.py** references an undefined `data` inside `f.write(data)` — appears to have intended the `date` variable. Preserved as-is for the learning record.
- The **AOP** section of `1110_2_AOP.py` is comment-only; class time ran out. Only the OOP part runs.
- The `195.168.9.x` range is a classroom LAN — not externally routable. Password `0000` is the Oracle XE classroom default.
