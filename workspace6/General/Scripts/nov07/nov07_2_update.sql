-- CRUD의 U: Update.
-- Update 테이블 set 필드 = 값, 필드 = 값...
--	where 조건;

SELECT * FROM 회사;

-- set의 활용: 특정 값으로 지정
UPDATE 회사
	SET 회사_직원수 = 50
		WHERE 회사_사명 = '오리온';

SELECT * FROM 제품 ORDER BY 제품_제품일련번호;


-- set의 활용: 기존 값 기준으로 연산
-- where 활용, 특정 조건에 해당하는 제품으로 범위 한정
UPDATE 제품
	SET 제품_가격 = 제품_가격 + 150
		WHERE 제품_제품명 LIKE '%새우%';

-- 실습: 본사 위치가 강남인 제품의 가격 10% 인상시키기

UPDATE 제품
	SET 제품_가격 = 제품_가격 * 1.1
		WHERE 제품_사명 IN (
			SELECT 회사_사명 FROM 회사 WHERE 회사_지역 = '강남'
		);

-- 이런 식으로 조건을 걸 때는 IN을 쓰자. = 은 결과가 여러 개여도 하나밖에 반환하지 못한다.

SELECT * FROM 제품 ORDER BY 제품_사명;


---------------------------------------------
-- D: Delete. 데이터를 특정 테이블에서 제거.

DELETE FROM 제품
 WHERE 제품_제품명 = '롯데샌드';

-- delete from 이 바로 연달아 나오는 것에 유의.


-- 실습: 유통기한이 지난 제품을 제품에서 제거.
DELETE FROM 제품
	WHERE 제품_유통기한 < sysdate;


-- 예제: 직원 수가 가장 적은 회사의 제품 삭제. (폐업!)

DELETE FROM 제품
	WHERE 제품_사명 IN (
		SELECT 회사_사명 FROM 회사
			WHERE 회사_직원수 = (
				SELECT min(회사_직원수)
					FROM 회사
			)
		);