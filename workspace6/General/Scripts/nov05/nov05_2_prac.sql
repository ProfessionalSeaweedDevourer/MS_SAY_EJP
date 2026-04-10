DROP TABLE nov05_student CASCADE CONSTRAINT purge;

CREATE TABLE nov05_student(
학번 number(2) PRIMARY KEY,
이름 varchar(12) NOT null,
국어 number(3) NOT NULL,
영어 number(3) NOT NULL,
수학 number(3) NOT null
);

-- ALTER TABLE nov05_student MODIFY (이름 varchar2(12));

INSERT INTO nov05_student VALUES(1, '홍길동', 100, 80, 90);
INSERT INTO nov05_student values(2, '김길동', 90, 50, 60);

SELECT * FROM nov05_student;
-- 그 자체로는 아무 의미도 없는데, primary key로 삼을 게 없어서 어거지로 만들어낸 학번 필드
-- 그런 주제에 이제 새로운 데이터를 입력할 때마다 이것도 세어서 추가해야 함
-- 하지만 oracledb에는 auto increment 옵션이 없고 다른 방식으로 구현: sequence
----------------------------------------------------------------------------------
-- sequence: 테이블 내용물과는 독립적인 존재. insert 실패해도 이 카운트는 올라감
-- 즉, 이것은 애초에 1,2,3 카운트를 위해서 쓰는 기능은 아님(그건 나중에)
-- 값 들어갈 자리에 시퀀스명.nextval 하여 자동 카운트
-- 카운트 초기화하려면 그냥 drop 하고 다시 create
CREATE SEQUENCE nov05_student_seq;

INSERT INTO nov05_student VALUES(nov05_student_seq.nextval, '홍길동', 100, 80, 90);
INSERT INTO nov05_student values(nov05_student_seq.nextval, '김길동', 10, 50, 60);
INSERT INTO nov05_student values(nov05_student_seq.nextval, '홍길동', 0, 0, 0);
INSERT INTO nov05_student values(nov05_student_seq.nextval, '최길동ㅇㅇㅇㅇㅇㅇㅇㅇ', 0, 0, 0);
INSERT INTO nov05_student values(nov05_student_seq.nextval, )

-- sysdate로 현재 시간을 입력할 수 있다.
-- to_date('값', '패턴'): 글자 -> 시간/날짜
-- to_date('1998-01-01 23', 'YYYY-MM-DD HH24')
-- 패턴: y/m/d/am/pm/hh/hh24/mi/ss 등 다양함

