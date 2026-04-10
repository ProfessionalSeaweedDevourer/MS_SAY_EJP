SELECT 이름, 유통기한, 가격 FROM nov05_snack2 WHERE 유통기한 <= sysdate;
-- to_date 없이 sysdate를 그대로 쓴다.
-- 그런데, sysdate는 현재 시각까지 반영하기 때문에 원래 묻고자 하는 것과는 결과가 다르다.
-- sysdate 중 '오늘 날짜의 23:59'를 입력해야 한다.

-- to_date(str, '패턴') : str를 date로 변환
-- to_char(date, '패턴') : date를 str로 변환
-- concat(str, str, ...): str 붙이기.
-- 이에 따라, sysdate를 to_char해서 날짜만 > 
-- 를 concat해서 23시 59분 붙이기 > 
-- 를 to_date해서 23시 59분 59초로 판정되게 하기. (우욱씹)

SELECT 이름, 유통기한, 가격
FROM nov05_snack2
WHERE 유통기한 <= to_date(
	concat(
		to_char(sysdate, 'yyyymmdd'), '235959'),
			'yyyymmdd hh24miss'
);

-- 실습: 가장 비싼 제품명 출력하기

SELECT 이름 FROM nov05_snack2 WHERE 가격 = 
(SELECT max(가격) FROM nov05_snack2);

-- 그룹 함수 그 자체를 where의 대상으로 삼을 수 없다.
-- select를 한 번 더 해서, max의 결과를 뽑아온 뒤에 where에 넣어야 한다. > subquery

-- 확장: 평균보다 저렴한 과자의 이름과 가격

SELECT 이름, 가격 FROM nov05_snack2 WHERE 가격 <=
	(SELECT avg(가격) FROM nov05_snack2);

-- 확장: 평균보다 비싼 과자들의 개수

SELECT count(*) FROM nov05_snack2 WHERE 가격 >
	(SELECT avg(가격) FROM nov05_snack2);