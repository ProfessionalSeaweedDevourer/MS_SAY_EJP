SELECT * FROM NOV06_CEO;
SELECT * FROM NOV06_RESTAURANT;
SELECT * FROM NOV06_MENU;
SELECT * FROM NOV06_RUN;

-- 평균가보다 싼 메뉴 
SELECT m_name FROM NOV06_MENU WHERE m_price < (SELECT avg(m_price) FROM NOV06_MENU);

-- 사장 이름, 매장명, 지점명, 메뉴명, 가격
SELECT c_name, r_name, r_jijum, m_name, m_price FROM NOV06_CEO nc, NOV06_RESTAURANT nr, NOV06_MENU nm;

-- 매장명 오름차순 + 메뉴명 오름차순 중 2-4번째 데이터
SELECT * FROM (
	SELECT rownum AS rn, r_name
		FROM (
			SELECT r_name FROM nov06_restaurant ORDER BY r_name ASC
		)
	)
WHERE rn >=2 AND rn <=4 ;


SELECT * FROM (
SELECT rownum AS rn, m_name, m_price
FROM (
	SELECT m_name, m_price FROM nov06_menu ORDER BY m_name, m_price DESC)
)
WHERE rn>=2 AND rn <=4;