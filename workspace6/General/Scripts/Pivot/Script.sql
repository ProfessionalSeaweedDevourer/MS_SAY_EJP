SELECT * FROM users;

ALTER TABLE users ADD (
  name VARCHAR2(100),
  role VARCHAR2(100),
  description VARCHAR2(500)
);

TRUNCATE TABLE users;

SELECT COUNT(*) AS CNT FROM user_tab_columns WHERE table_name='USERS' AND column_name='PROFILE_IMAGE_MIME'

ALTER TABLE users ADD (profile_image_filename VARCHAR2(255), profile_image_mime VARCHAR2(100))