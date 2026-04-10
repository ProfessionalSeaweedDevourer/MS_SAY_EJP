-- CRUD 중 R은 CUD 전체와 동등하게 배울 게 많다.

CREATE SEQUENCE nov05_snack2_seq;

CREATE TABLE nov05_snack2(
	번호 number(3) PRIMARY KEY,
	이름 varchar(24) NOT NULL,
	유통기한 DATE NOT NULL,
	가격 number(5) NOT NULL,
	중량 number(6,2) NOT NULL
);

INSERT INTO nov05_snack2 VALUES (nov05_snack2_seq.nextval, '초코파이', to_date('2025-12-01', 'YYYY-MM-DD'), 5000, 300.52);
INSERT INTO NOV05_SNACK2 VALUES (NOV05_SNACK2_SEQ.NEXTVAL, '포카칩', to_date('2025-12-12', 'yyyy-mm-dd'), 3500, 150.5);
INSERT INTO NOV05_SNACK2 VALUES (NOV05_SNACK2_SEQ.NEXTVAL, '고래밥', to_date('2025-11-12', 'yyyy-mm-dd'), 2400, 100.25);
INSERT INTO NOV05_SNACK2 VALUES (NOV05_SNACK2_SEQ.NEXTVAL, '썬칩', to_date('2025-12-08', 'yyyy-mm-dd'), 3500, 180.35);
INSERT INTO NOV05_SNACK2 VALUES (NOV05_SNACK2_SEQ.NEXTVAL, '프링글스', to_date('2025-12-12', 'yyyy-mm-dd'), 4300, 250.5);
INSERT INTO NOV05_SNACK2 VALUES (NOV05_SNACK2_SEQ.NEXTVAL, '츄파춥스', to_date('2026-01-12', 'yyyy-mm-dd'), 300, 20.5);
INSERT INTO nov05_snack2 VALUES (nov05_snack2_seq.nextval, '도리토스', to_date('2026-08-03', 'yyyy-mm-dd'), 3800, 300);

INSERT INTO nov05_snack2 VALUES (nov05_snack2_seq.nextval, '빼빼로', to_date('2026-08-03', 'yyyy-mm-dd'), 2500, 150);
INSERT INTO nov05_snack2 VALUES (nov05_snack2_seq.nextval, '말차빼빼로', to_date('2026-08-03', 'yyyy-mm-dd'), 2500, 150);
INSERT INTO nov05_snack2 VALUES (nov05_snack2_seq.nextval, '딸기빼빼로', to_date('2025-11-06', 'yyyy-mm-dd'), 2500, 150);

SELECT * FROM nov05_snack2;

SELECT 이름, 가격 FROM nov05_snack2;

SELECT 이름, 유통기한 FROM nov05_snack2;

SELECT 이름, 가격, 중량 FROM nov05_snack2;

-- 표기 카테고리명 바꾸기
SELECT 이름 AS 상품명, 가격 AS 소비자가격 FROM nov05_snack2;

-- 수치 간 연산하기: 전체 데이터를 가져와서 연산하고 다시 넣는 것보다 나음
-- 가령, g당 가격을 연산해서 출력하는 것이 가능.
SELECT 이름, 중량/가격 AS 단위가격 FROM nov05_snack2;

-- 예제: 이름, 가격, vat 조회

SELECT 이름, 가격, 가격/10 AS VAT FROM nov05_snack2;

-- 나아가, 통계 연산을 수행하는 함수도 있다.
-- sum(필드), avg(필드), max(), min(), count() 등.

SELECT max(가격) AS 최고가, min(가격) AS 최저가, count(이름) AS 종류 FROM nov05_snack2;
-- 생각해 보면 count()는 어디를 기준으로 해도 별로 상관이 없음. 그래서 count(*)도 먹힘.
-- avg()와 같이 따로 나오는 값과 기존 데이터를 함께 출력할 수는 없음. 모양이 안 잡히니까
-- 하여튼, select와는 필드명, 필드명 as 별칭, 연산자, 통계함수 사용 가능.

SELECT 이름, 가격 FROM nov05_snack2;

-- 조건 달아서 검색하기

SELECT 이름, 가격 FROM nov05_snack2 WHERE 가격<=3000;

SELECT count(*) FROM nov05_snack2 WHERE 가격>=5000;

SELECT 가격 FROM nov05_snack2 WHERE 이름 = '썬칩';

-- 특정 문자열 포함을 조건으로 검색하기(and, or도 사용 가능)

SELECT 이름 FROM nov05_snack2 WHERE 이름 LIKE '%빼빼로%';

-- 실습

SELECT 이름, 가격 FROM nov05_snack2 WHERE 가격 > 5000 OR 가격 < 2000;

SELECT 이름, 가격, 가격/10 AS VAT FROM nov05_snack2 WHERE 가격 > 2000 AND 가격 < 5000;
-- between을 써서 구현하는 것도 가능하다. (그러던가 말던가)

SELECT 이름, 유통기한 FROM nov05_snack2 WHERE 유통기한 > to_date('2025-11-01','yyyy-mm-dd') AND 유통기한 < to_date('2025-12-01', 'yyyy-mm-dd');
