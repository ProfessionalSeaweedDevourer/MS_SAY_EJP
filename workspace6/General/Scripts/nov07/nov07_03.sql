CREATE TABLE nov07_restaurant(
	r_no number(3) PRIMARY KEY,
	r_name varchar2(10 char) NOT NULL,
	r_loc varchar2(10 char) NOT NULL,
	r_tablecnt number(3) NOT NULL
);

CREATE SEQUENCE nov07_restaurant_seq;

INSERT INTO nov07_restaurant values(nov07_restaurant_seq.nextval, '김밥천국', '종로', 10);
INSERT INTO nov07_restaurant values(nov07_restaurant_seq.nextval, '역전우동', '강남', 20);

SELECT * FROM nov07_restaurant;

CREATE SEQUENCE nov07_menu_seq;

CREATE TABLE nov07_menu(
	m_no number(3) PRIMARY KEY,
	m_name varchar2(10 char) NOT NULL,
	m_price NUMBER(5) NOT NULL,
	m_cate varchar2(10 char) NOT NULL,
	m_r_no NUMBER(3) NOT NULL,
	CONSTRAINT menu_restaurant
		FOREIGN KEY (m_r_no) REFERENCES nov07_restaurant(r_no) -- 괄호 필수!
		ON DELETE CASCADE -- 원본 삭제 시 같이 떨어지게 설정
);

SELECT * FROM nov07_menu;

INSERT INTO nov07_menu values(nov07_menu_seq.nextval, '야채김밥', 4000, '식사', 1);
INSERT INTO nov07_menu values(nov07_menu_seq.nextval, '튀김우동', 5000, '식사', 2);

INSERT INTO nov07_menu values(nov07_menu_seq.nextval, '비빔밥', 5000, '식사', 3);
-- 3번은 식당 테이블에 존재하지 않으므로 오류 발생.

-- 외래키
-- 1) 메뉴 테이블에서의 '매장 번호'는, 식당 테이블의 매장 번호에 실제로 존재하는 값만 가질 수 있도록 하기.
-- 2) 식당 테이블에서 사라진 '매장'의 메뉴는 메뉴 테이블에서도 자동으로 같이 없어지게 하기 > cascade?

DELETE FROM nov07_restaurant WHERE r_name = '김밥천국' AND r_loc = '종로';