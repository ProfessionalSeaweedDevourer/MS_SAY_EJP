# 📁 Python & Oracle DB 연동 프로젝트 가이드 (MWM 프로젝트)
본 프로젝트는 기본적인 ***Model-View-Controller (MVC)*** 디자인 패턴을 기반으로 구축되었습니다. 각 스크립트 파일은 명확한 역할을 수행하며, 데이터베이스 연동에는 oracledb 라이브러리와 RETURNING INTO 기법을 사용하여 안정적인 트랜잭션을 구현합니다.

## 1. 🏛️ 프로젝트 구조 및 MVC 역할 분리
애플리케이션의 핵심 로직을 Model, View, Controller 세 부분으로 분리하여 유지보수성과 확장성을 높입니다.

- homeController.py: ***Controller 담당***. App의 흐름 제어 & 중제. View를 호출해 입력을 받고, 이를 다시 Model에 전달해 작업을 지시한 후 그 결과를 View로 전달.
- consoleScreen.py: ***View 담당***. 사용자에게 데이터 입력 프롬프트를 제공하고, 최종 처리 결과를 화면에 출력.
- mwmDAO.py: ***Model 담당***. 비즈니스 로직 및 데이터 접근 담당. oracledb를 사용해 DB 통신 및 트랜잭션 관리.
- ejp_lib/ejpDBManager.py: DB 연결 생성 및 해제 등 인프라 담당 유틸리티 클래스.
- seller.py & product.py: DB 테이블의 실제 레코드를 담는 데이터 객체.

## 2. 🗄️ 데이터베이스 스키마 및 주요 제약 조건

* ON DELETE CASCADE: 판매자(MWM_SELLER)가 삭제되면, 해당 판매자가 등록한 모든 제품(MWM_PRODUCT)은 자동으로 삭제됩니다.

| 테이블명 | 기본 키 | 외래 키 | 제약 조건 |
|:---|:---|:---|:---|
| MWM_SELLER | SELLER_NO (시퀀스) | - | - |
| MWM_PRODUCT | PRODUCT_ID (시퀀스) | SELLER_NO (판매자 테이블로부터) | (SELLER_NO, PRODUCT_NAME) |