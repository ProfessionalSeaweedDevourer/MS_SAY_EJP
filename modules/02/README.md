# Module ② — Data Ingestion (Crawling · Public APIs)

> **[🇰🇷 한국어](#-한국어)** · **[🇺🇸 English](#-english)**

---

## 🇰🇷 한국어

정적 HTML 크롤링 → 브라우저 DOM/JQuery 파싱 → 공공 API · 외부 서비스 API 호출까지, **"외부 세계에서 데이터를 끌어오는 방법"** 을 단계적으로 실습한 구간입니다. `C01_python/` 과 `C02_web/` 두 과정에 걸쳐 있습니다.

### 🗂 포함 디렉토리

| 경로 | 주제 |
|---|---|
| [../../C01_python/1103_pyWebcrawl/](../../C01_python/1103_pyWebcrawl/) | Python `requests` · `BeautifulSoup` 기반 정적 크롤링 |
| [../../C02_web/1118_css_and_pyWebcrawl/](../../C02_web/1118_css_and_pyWebcrawl/) | CSS 셀렉터 기반 파싱 실습 |
| [../../C02_web/1128_HTML5_game_JQ_webparse/](../../C02_web/1128_HTML5_game_JQ_webparse/) | jQuery 로 웹 데이터 파싱 |
| [../../C02_web/1201_Webparse_ExternalAPI/](../../C02_web/1201_Webparse_ExternalAPI/) | 외부 API 연동 파싱 |
| [../../C02_web/1202_KakaomapAPI_and_JQMobile/](../../C02_web/1202_KakaomapAPI_and_JQMobile/) | Kakao Map API · jQuery Mobile |

### 🎯 핵심 학습 주제

- HTTP 요청/응답 모델, User-Agent·Referer 헤더 제어
- CSS 셀렉터 · XPath 로 DOM 트리 탐색
- 공공 데이터 포털 · Kakao Map 등 외부 API 키 발급·호출·응답 파싱
- 동기(requests) vs 비동기(JS/jQuery AJAX) 수집 방식 차이

### 🔁 재현 주의

- 일부 대상 사이트는 크롤링 방어(Cloudflare·동적 렌더링)가 강화되어 당시 코드가 현재는 실패할 수 있습니다.
- Kakao/공공 API 키는 저장소에 포함되지 않습니다. 본인 앱 키로 교체 필요.

---

## 🇺🇸 English

A staged exploration of "how to pull data from the outside world": static HTML crawling → browser DOM / jQuery parsing → public-data and third-party API calls. This module straddles the `C01_python/` and `C02_web/` course folders.

### 🗂 Included Directories

| Path | Topic |
|---|---|
| [../../C01_python/1103_pyWebcrawl/](../../C01_python/1103_pyWebcrawl/) | Static crawling with `requests` · `BeautifulSoup` |
| [../../C02_web/1118_css_and_pyWebcrawl/](../../C02_web/1118_css_and_pyWebcrawl/) | CSS-selector-driven parsing |
| [../../C02_web/1128_HTML5_game_JQ_webparse/](../../C02_web/1128_HTML5_game_JQ_webparse/) | Web scraping via jQuery |
| [../../C02_web/1201_Webparse_ExternalAPI/](../../C02_web/1201_Webparse_ExternalAPI/) | External-API parsing |
| [../../C02_web/1202_KakaomapAPI_and_JQMobile/](../../C02_web/1202_KakaomapAPI_and_JQMobile/) | Kakao Map API · jQuery Mobile |

### 🎯 Key Topics

- HTTP request/response model, User-Agent / Referer header handling
- DOM traversal using CSS selectors · XPath
- Registering, calling, and parsing responses from public-data portals and Kakao Map
- Synchronous (`requests`) vs. asynchronous (JS/jQuery AJAX) ingestion

### 🔁 Reproduction Notes

- Some target sites have since hardened their anti-scraping defenses (Cloudflare, dynamic rendering); the original code may no longer succeed.
- Kakao / public-data API keys are not committed — supply your own app keys.
