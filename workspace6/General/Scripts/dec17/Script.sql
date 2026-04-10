CREATE TABLE dec17_menu(
	m_name varchar2(30 char) PRIMARY KEY,
	m_price number(5) NOT NULL,
	m_desc varchar2(100 char) NOT null
);

INSERT INTO dec17_menu values('라면', 3500, '신라면');

SELECT * FROM dec17_menu;