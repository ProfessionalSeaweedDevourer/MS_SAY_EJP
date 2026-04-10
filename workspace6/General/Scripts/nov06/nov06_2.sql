CREATE TABLE 지점장 (
	이름 varchar2(12) PRIMARY KEY,
	매장 varchar2(18) NOT NULL,
	지점 varchar2(21) NOT NULL,
	테이블 number(3) NOT NULL,
	메뉴 varchar2(21) NOT NULL,
	가격 number(6) NOT NULL,
	분류 varchar2(18) NOT NULL
);

DROP TABLE 지점장 CASCADE CONSTRAINT purge;

INSERT INTO 지점장 VALUES ('홍길동, ')

-- 테이블의 정규화: 현재 구조대로라면, 메뉴가 추가될 때마다 한 줄을 늘려야 해서 대량의 중복 데이터가 생김.
-- DBMS
--		RDBMS 계열: OrcaleDB, MySQL, MariaDB, SQLite...
--		NoSQL 계열: MongoDB, ...
---------------------------------------------------------
-- 테이블의 설계
-- 1) 주제별로 테이블을 나누고, 2) 기본키를 선정, 3) 테이블 간 관계 고려.
-- 1) '사장'의 정보, '매장'의 정보, '메뉴'의 정보를 개별 테이블로 만들자.
-- 2)
-- 3) 1:n의 경우, n쪽 테이블에 1쪽 테이블의 기본키를 하나의 필드로 넣는다.
-- 		e.g) 메뉴 테이블의 각 원소는 '판매하는 매장 번호'를 갖는다.
--	  m:n의 경우, 양쪽 테이블의 기본키 둘을 원소로 갖는 별도의 테이블을 만든다.
--		e.g) 매장과 사장의 일련번호를 갖는 테이블을 만든다.


-- 3-1) 매장과 메뉴의 관계는 매장 사정에 따라 다르다. 일단 식당: 메뉴를 1:n으로 상정.
-- 3-2) 사장과 매장의 관계는 n:m. 여러 개를 경영할 수도 있고, 하나의 프랜차이즈가 여러 지점 / 지점장을 가진다.
-- 3-3) 사장과 메뉴의 관계는...n:m?

-- 시퀀스는 예외가 발생해도 카운트가 올라가기 때문에, 데이터 입력 시 순서가 중요해진다.
-- 

CREATE SEQUENCE 사업자번호;
CREATE SEQUENCE 매장번호;
CREATE SEQUENCE 메뉴번호;
CREATE SEQUENCE 사장메뉴번호;

CREATE TABLE 사장 (
	사업자번호 NUMBER(3) PRIMARY KEY,
	이름 varchar2(12) NOT null,
	생년월일 DATE NOT NULL,
	거주지 varchar(21) NOT null
);

DROP TABLE 사장 CASCADE CONSTRAINT purge;

INSERT INTO 사장 values(사업자번호.nextval, '홍길동', to_date('19990101','yyyy-mm-dd'), '수원');
INSERT INTO 사장 values(사업자번호.nextval, '김길동', to_date('20000303','yyyy-mm-dd'), '안양');


CREATE TABLE 매장 (
	매장번호 number(3) PRIMARY KEY,
	프랜차이즈 varchar(21) NOT NULL,
	지점명 varchar(21) NOT NULL,
	테이블수 number(3) NOT NULL 
);

DROP TABLE 매장 CASCADE CONSTRAINT purge;

INSERT INTO 매장 values(매장번호.nextval, '김밥천국', '종로', 10);
INSERT INTO 매장 values(매장번호.nextval, '김밥천국', '서초', 20);
INSERT INTO 매장 VALUES(매장번호.nextval, '역전우동', '종로', 15);

CREATE TABLE 메뉴 ( 
	메뉴번호 number(3) PRIMARY KEY,
	메뉴명 varchar(21) NOT NULL,
	가격 number(6) NOT NULL,
	분류 varchar(15) NOT NULL
);

DROP TABLE 메뉴 CASCADE CONSTRAINT purge;

ALTER TABLE 메뉴 ADD 매장번호 number(3);

-- 1. 매장번호 컬럼에 외래 키 제약 조건 추가
ALTER TABLE 메뉴
ADD CONSTRAINT fk_메뉴_매장번호
FOREIGN KEY (매장번호)
REFERENCES 매장 (매장번호);

SELECT 매장번호, 프랜차이즈, 지점명 FROM 매장;

-- 2. 외래 키 설정 후 데이터 삽입
INSERT INTO 메뉴 (메뉴번호, 메뉴명, 가격, 분류, 매장번호)
VALUES (메뉴번호.nextval, '야채김밥', 4000, '식사류', 24);
INSERT INTO 메뉴 values(메뉴번호.nextval, '비빔밥', 5000, '식사류', 25);
INSERT INTO 메뉴 values(메뉴번호.nextval, '우동', 4500, '식사류', 26);
INSERT INTO 메뉴 values(메뉴번호.nextval, '비빔밥', 5500, '식사류', 26);
INSERT INTO 메뉴 values(메뉴번호.nextval, '카스', 6000, '주류', 24);

CREATE TABLE 등록 (
    등록번호 number(3) PRIMARY KEY,
    등록_사장번호 number(3) NOT NULL,
    등록_매장번호 number(3) NOT null,
    CONSTRAINT fk_등록_사장번호 FOREIGN KEY (등록_사장번호) REFERENCES 사장 (사업자번호),
    CONSTRAINT fk_등록_매장번호 FOREIGN KEY (등록_매장번호) REFERENCES 매장 (매장번호)
);

DROP TABLE 등록 CASCADE CONSTRAINT purge;

INSERT INTO 등록 (등록번호, 등록_사장번호, 등록_매장번호)
SELECT 등록번호.NEXTVAL, S.사업자번호, M.매장번호
FROM 사장 S
CROSS JOIN 매장 M;

SELECT * FROM 사장;
SELECT * FROM 매장;
SELECT * FROM 메뉴;
SELECT * FROM 등록;

SELECT 메뉴명, 가격 FROM 메뉴;

SELECT 지점명, 테이블수 FROM 매장 WHERE 프랜차이즈 = '김밥천국';

SELECT avg(가격) AS 평균가 FROM 메뉴;

SELECT avg(가격) AS 식사평균가 FROM 메뉴 WHERE 분류 = '식사류';

SELECT 이름, 생년월일 FROM 사장 WHERE 생년월일 = (SELECT min(생년월일) FROM 사장);


-- 김천 종로의 메뉴
SELECT 메뉴명, 가격 FROM 메뉴 WHERE 매장번호 = (SELECT 매장번호 FROM 매장 WHERE 프랜차이즈 = '김밥천국' AND 지점명 = '종로');

-- 가장 나이 많은 사장의 매장 / 지점

SELECT 프랜차이즈, 지점명 FROM 매장 WHERE 매장번호 = (
	SELECT 매장번호 FROM 등록 WHERE 등록_사장번호 = (
	SELECT 사업자번호 FROM 사장 WHERE 생년월일 = (
			SELECT min(생년월일) FROM 사장
		)
	)
);


-- 테이블이 가장 많은 매장의 사장
-- > join을 활용해 해결하기.
-- > join 시 발생하는 문제를 해결하기 위해, 각 데이터별 속성명을 확실히 구분할 수 있도록 이름짓기.

SELECT * FROM 매장, 메뉴, 등록;