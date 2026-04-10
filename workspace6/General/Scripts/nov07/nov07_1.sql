---------------------------------------------------------------------------------------------------------------------
-- 오늘의 주제: 마트에서의 과자 재고 관리

-- (지역) 지역의 사장 (사장이름), (회사명)의 직원 (직원수)명.

-- 이 회사 (회사명)에서 만드는 과자 (제품명)의 가격 (가격), 무게 (무게), 유통기한 (날짜).

-- 테이블의 설계
-- 1) 주제별로 테이블을 나누고, 2) 기본키를 선정, 3) 테이블 간 관계 고려.

-- '회사' 당 '사장'과 '지점'은 하나.
-- '회사' 당 '제품'은 여러 개. 그러나, '제품' 역시 동일한 이름으로 여러 '회사'에서 생산될 수 있음.

-- 테이블은 '회사' 와 '제품'.
-- '회사'는 회사명, 위치, 사장, 직원 수를 가짐. 회사명이 기본키.
-- '제품'은 자체 카운트를 기본키로 갖고, 제품명, 가격, 무게, 유통기한, 생산하는 회사를 가짐.

CREATE SEQUENCE 제품일련번호;

-- 회사명과 생산 회사 번호를 원소로 갖는 '생산' 테이블.

-- 3) 1:n의 경우, n쪽 테이블에 1쪽 테이블의 기본키를 하나의 필드로 넣는다.
-- 		e.g) 메뉴 테이블의 각 원소는 '판매하는 매장 번호'를 갖는다.
--	  m:n의 경우, 양쪽 테이블의 기본키 둘을 원소로 갖는 별도의 테이블을 만든다.
--		e.g) 매장과 사장의 일련번호를 갖는 테이블을 만든다.

CREATE TABLE 회사 (
	회사_사명 varchar2(18 char) PRIMARY KEY,
	회사_사장 varchar2(18 char) NOT NULL,
	회사_지역 varchar2(18 char) NOT NULL,
	회사_직원수 number(5) NOT NULL
);

CREATE TABLE 제품 (
	제품_제품일련번호 number(5) PRIMARY KEY,
	제품_제품명 varchar2(21 char) NOT NULL,
	제품_가격 number(5) NOT NULL,
	제품_무게 NUMBER(5,2) NOT NULL,
	제품_유통기한 DATE NOT NULL
);

ALTER TABLE 제품
ADD (
    제품_사명 varchar2(18 char) NOT NULL
);

ALTER TABLE 제품
ADD CONSTRAINT FK_제품_사명
FOREIGN KEY (제품_사명)
REFERENCES 회사(회사_사명);

INSERT INTO 회사 values('오리온', '홍길동', '강남', 100);
INSERT INTO 회사 values('롯데', '김철수', '종로', 50);
INSERT INTO 회사 values('농심', '외계인', '강북', 300);
INSERT INTO 회사 values('해태', '이해태', '수원', 250);

INSERT INTO 제품 values(제품일련번호.nextval, '초코파이', 3500, 350.50, to_date('20260331','yyyy-mm-dd'), '오리온');
INSERT INTO 제품 values(제품일련번호.nextval, '초코파이', 4300, 420.30, to_date('20260220','yyyy-mm-dd'), '롯데');
INSERT INTO 제품 values(제품일련번호.nextval, '새우깡', 3200, 250.5, to_date('20260811', 'yyyy-mm-dd'), '농심');
INSERT INTO 제품 values(제품일련번호.nextval, '새우깡', 2700, 210, to_date('20260615', 'yyyy-mm-dd'), '해태');
INSERT INTO 제품 values(제품일련번호.nextval, '초코파이', 5500, 450, to_date('20260307', 'yyyy-mm-dd'), '오리온');
INSERT INTO 제품 values(제품일련번호.nextval, '꿀꽈배기', 3300, 260, to_date('20260110', 'yyyy-mm-dd'), '농심');
INSERT INTO 제품 values(제품일련번호.nextval, '홈런볼', 2800, 220, to_date('20251223', 'yyyy-mm-dd'), '해태');

SELECT * FROM 회사;
SELECT * FROM 제품;

-- 1) 전체 과자의 이름과 가격
SELECT 제품_제품명, 제품_가격 FROM 제품;

-- select distinct를 통해 '같은 것'은 여러 번 나오지 않게 출력할 수 있다.

-- 2) 과자 평균가 산출
SELECT avg(제품_가격) AS 평균가 FROM 제품;
-- 자릿수 조절이 가능한지?

-- 3) 최고 가격을 가진 과자의 이름과 그 가격
SELECT 제품_제품명, 제품_가격 FROM 제품 WHERE 제품_가격 = (SELECT max(제품_가격) FROM 제품);

-- 4) 유통기한이 지난 과자의 수
SELECT count(*) AS 폐기 FROM 제품 WHERE 제품_유통기한 < sysdate;

-- 5) 최저가 과자를 생산하는 회사의 이름과 그 지역
SELECT 회사_사명, 회사_지역 FROM 회사
	JOIN 제품 ON 회사.회사_사명 = 제품.제품_사명
		WHERE 제품.제품_가격 = (SELECT MIN(제품_가격) FROM 제품);

-- 다른 답안
SELECT 회사_사명, 회사_지역 FROM 회사
	WHERE 회사_사명 IN (
		SELECT 제품_사명 FROM 제품
			WHERE 제품_가격 = (
				SELECT min(제품_가격)
			) FROM 제품
		);

-- 6) 직원 수가 가장 많은 회사의 과자(들) 이름과 그 가격
SELECT
    제품.제품_제품명,
    제품.제품_가격
FROM
    회사
JOIN
    제품 ON 회사.회사_사명 = 제품.제품_사명 -- 사명(외래 키)을 기준으로 두 테이블 연결
WHERE
    회사.회사_직원수 = (SELECT MAX(회사_직원수) FROM 회사); -- 직원 수가 최대인 회사만 필터링
    
-- 7) 유통기한이 가장 많이 남은 순서대로, 그 각각을 가나다순으로 정렬.
    
SELECT * FROM 제품 ORDER BY 제품_유통기한 DESC, 제품_제품명 ASC;

-- 8) 회사별 제품 평균가
SELECT 제품_사명, avg(제품_가격) FROM 제품 GROUP BY 제품_사명;

-- 9) 제품명별 재고
SELECT 제품_제품명, 제품_재고 FROM 제품 GROUP BY 제품_제품명;

-- 10) 사장 이름별 / 회사 사명별 과자 최고가

SELECT 회사_사장, 회사_사명, max(제품_가격)
	FROM 회사, 제품
		WHERE 회사_사명 = 제품_사명
	GROUP BY 회사_사장, 회사_사명
	ORDER BY 회사_사장, 회사_사명;

-- 11) 가격이 3,000 이상인 제품에 한한 회사별 제품 평균가

SELECT 제품_사명, avg(제품_가격) FROM 제품 
	WHERE 제품_가격 > 3000
GROUP BY 제품_사명;

-- 이렇게 하면 평균을 먼저 구하고 연산되지 않나? << 범위를 정하는 from/where가 항상 가장 먼저 선택됨.

-- 12) 가격이 5,000 이상인 제품에 한한 회사별 제품 평균가

SELECT 제품_사명, avg(제품_가격) FROM 제품 WHERE 제품_가격>=5000 GROUP BY 제품_사명;

-- 13) 회사별 과자 평균, 단 그 중 결과가 4,000 이상인 것만.
SELECT 제품_사명, 평균가 FROM (
SELECT 제품_사명, avg(제품_가격) AS 평균가 FROM 제품 GROUP BY 제품_사명 
)
WHERE 평균가 >= 4000;

-- 원래 답안 (group by의 자체 조건으로 having 활용)
SELECT 제품_사명, avg(제품_가격) FROM 제품 GROUP BY 제품_사명 HAVING avg(제품_가격) >= 4000;

-- 사장 이름 / 회사별로 단위 무게당 평균가. 단, 가격이 1,000 미만인 것은 제외.
SELECT
    A.회사_사장,
    B.제품_사명,
    AVG(B.제품_가격 / B.제품_무게) AS 단위평균가
FROM
    회사 A
JOIN
    제품 B ON A.회사_사명 = B.제품_사명 -- 1. 조인 조건 필수
WHERE
    B.제품_가격 >= 1000 -- 3. 개별 제품 가격 필터링 (1,000 미만 제외)
GROUP BY
    A.회사_사장,
    B.제품_사명 -- 2. 회사별 집계를 위해 사장, 사명으로 그룹화
HAVING
    AVG(B.제품_가격 / B.제품_무게) > 10; -- (선택) 만약 단위 평균가에 대한 추가 필터링이 필요하다면 사용