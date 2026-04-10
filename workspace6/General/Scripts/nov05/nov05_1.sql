-- 테스트 주석
-- sql 문법은 대문자가 되어버리기 때문에
-- 낙타체는 쓸 수가 없다 (dogName > DOGNAME)

-- 일반 개발자 입장에서는 CRUD만 다룰 것
-- Create / Read / Update / Delete
-------------------------------------------
-- table에 대해
-- 가로줄: 행(row), record, data
-- 세로줄: 열(column), field
-------------------------------------------
-- 오라클 db는 자료형을 정할 수 있다.
-------------------------------------------
-- 글자:
-- 		char(용량): 무조건 정해진 용량만큼만 저장
--		varchar2(용량): 자동으로 용량 조절
-- 예를 들어 char(5 char)에 'ㅋㅋㅋ'를 저장하면 > 'ㅋㅋㅋ  '가 들어감
-- 빠르지만 용량 낭비 발생 > 모든 데이터 글자 수가 같은 게 보장되면 유용
-- varchar2(5 char)에 저장하면 'ㅋㅋㅋ'만 들어감
-- 추가 연산 부담이 있는 varchar를 좀 더 개선한 버전. 일반적으로 사용
-------------------------------------------
-- 숫자:
--		number(용량): 자릿수(예: 5 > 99999)
--		number(5,2): 총 5자리, 그 중 소숫점 2자리
-- 날짜/시간: date
-- 파일: 파일 그 자체는 db가 아니라 실제 구동 서버에 넣기. 너무 크니까

-----------------------------------------------
-- 테이블 생성
CREATE TABLE nov05_snack(
	s_name varchar2(10 char),
	s_price number(6)
);
----------------------------------------------
-- 데이터 삽입
--INSERT INTO 테이블명(필드명, 필드명, ...)
--VALUES(값, 값, ..);
INSERT INTO nov05_snack(s_name, s_price) VALUES('초코파이', 5000);

INSERT INTO nov05_snack(s_name, s_price) VALUES('빼빼로', 1500);

-- 순서를 다르게 하는 것도 가능. (왜 이런 짓을)
INSERT INTO nov05_snack(s_price, s_name) values(2500, '말차빼빼로');

-- 특정 필드는 값 안 넣어도 무방. > not null 걸면 불가
INSERT INTO nov05_snack(s_name) VALUES('칙촉');

-- 사실 그냥 순서대로 쓰면 알아서 들어감.
INSERT INTO nov05_snack VALUES('마이쮸', 500);
----------------------------------------------
-- 데이터 조회
SELECT * FROM nov05_snack;

----------------------------------------------
-- 테이블 삭제
DROP TABLE nov05_SNACK CASCADE CONSTRAINT purge;

----------------------------------------------
-- 옵션
--		not null: 필수
--		primary key: not null + 중복값 불허 >> 데이터의 '대표 값'.

CREATE TABLE NOV05_SNACK(
	s_name varchar2(10 char) PRIMARY KEY, -- 중복 불허
	s_price number(6) NOT NULL
);

INSERT INTO NOV05_SNACK VALUES('포카칩', 3500);
INSERT INTO NOV05_SNACK VALUES('포카칩', 5500); -- 이름은 primary key라 에러 뜸
INSERT INTO NOV05_SNACK values('새우깡', 3500);


SELECT * FROM NOV05_SNACK WHERE S_NAME = '초코파이';
SELECT * FROM NOV05_SNACK WHERE S_PRICE = 3500;