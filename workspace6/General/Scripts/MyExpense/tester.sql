INSERT INTO my_category VALUES (my_category_seq.nextval, '식비');

INSERT INTO my_exp VALUES (my_exp_seq.nextval, sysdate, '11/12 점심', 7000, 1);

SELECT * FROM my_exp;
SELECT * FROM my_category;

TRUNCATE TABLE my_exp;