CREATE TABLE OWMW (
    owmw_date       DATE            NOT NULL,  -- sysdate가 삽입됨 (날짜/시간)
    owmw_weather    VARCHAR2(50),              -- 날씨 설명 (예: '맑음')
    owmw_temp       NUMBER(5, 2),              -- 온도 (예: 15.34)
    owmw_humidity   NUMBER(3, 0)               -- 습도 (예: 60)
);