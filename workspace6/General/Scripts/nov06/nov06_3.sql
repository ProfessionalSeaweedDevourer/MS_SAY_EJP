-- 본격적인 join 활용 예시
-- 테이블이 가장 많은 매장의 사장 이름 구하기

SELECT * FROM nov06_ceo;
SELECT * FROM nov06_run;
SELECT * FROM NOV06_RESTAURANT;
SELECT * FROM nov06_menu;

SELECT c_name FROM nov06_ceo, nov06_run, nov06_restaurant
WHERE c_no = r_c_no AND r_r_no = nov06_restaurant.r_no AND r_table = (
	SELECT max(r_table) FROM nov06_restaurant
);

-- 하지만, 실무 관점에서 이는 좋지 못한 활용이다.
-- subquery는 대상 데이터를 줄이지만, join은 기하급수적으로 대상 데이터가 늘어난다.
-- join은 가능한 한 적게 쓸 방법을 생각해 내야 한다.

-- 예제: 테이블 수가 가장 많은 매장의 매장명, 지점명, 메뉴명, 가격 보기 > 이런 건 가능한 한 따로 보는 게 나음 
-- 요구사항이 영 어쩔 수 없으면...
SELECT c_name, r_name, m_name, m_price FROM nov06_ceo, nov06_run, nov06_restaurant, nov06_menu
WHERE c_no = r_c_no AND r_r_no = nov06_restaurant.r_no AND r_r_no = m_r_no
ORDER BY r_name;
; -- 크아악

-- 정렬: where ~ 뒤에 order by 필드명;
-- 기본 오름차순. 내림차순으로 하고 싶으면 필드명 뒤에 desc;

-- 예제: 테이블 수가 평균보다 많은 매장의 메뉴명과 가격

SELECT m_name, m_price FROM nov06_menu WHERE m_r_no IN (
	SELECT r_no FROM nov06_restaurant WHERE r_table > (SELECT avg(r_table) FROM nov06_restaurant) )
ORDER BY m_price DESC, m_name;


-- rownum: select 시마다 부여되는 가상의 필드. *와 동시 사용 불가.
-- order by 보다 먼저 부여됨.
-- 특정 위치 접근이 가능하지만, 1번부터 조회해야 함.

SELECT * FROM ( -- select를 한 겹 더 해서, rownum을 rownum이 아니게 받아서 해결.
SELECT rownum AS rn, m_name, m_price
FROM (
	SELECT m_name, m_price FROM nov06_menu ORDER BY m_name, m_price DESC)
)
WHERE rn>=3 AND rn <=5;