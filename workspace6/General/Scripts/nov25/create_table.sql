CREATE TABLE nov25_cnfood(
	f_name varchar2(10 char) PRIMARY KEY,
	f_price number(5) NOT NULL
);

INSERT INTO nov25_cnfood VALUES ('송이밥', 11000);
INSERT INTO nov25_cnfood VALUES ('마파두부밥', 9500);
INSERT INTO nov25_cnfood VALUES ('삼선짬뽕', 10000);
INSERT INTO nov25_cnfood VALUES ('짜장면', 7500);

SELECT * FROM nov25_cnfood;