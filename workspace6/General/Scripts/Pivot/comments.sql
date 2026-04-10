-- Migration: add posts/comments tables and user counters

-- Add counters to users if missing
BEGIN
  EXECUTE IMMEDIATE 'ALTER TABLE users ADD (post_count NUMBER DEFAULT 0)';
EXCEPTION
  WHEN OTHERS THEN
    IF SQLCODE != -1430 THEN RAISE; END IF; -- ignore column already exists
END;

BEGIN
  EXECUTE IMMEDIATE 'ALTER TABLE users ADD (comment_count NUMBER DEFAULT 0)';
EXCEPTION
  WHEN OTHERS THEN
    IF SQLCODE != -1430 THEN RAISE; END IF;
END;

-- Create posts table
BEGIN
  EXECUTE IMMEDIATE '
    CREATE TABLE posts (
      id VARCHAR2(36) PRIMARY KEY,
      author_id VARCHAR2(50),
      content CLOB,
      created_at VARCHAR2(50)
    )'
; EXCEPTION WHEN OTHERS THEN NULL; END;

-- Create comments table
BEGIN
  EXECUTE IMMEDIATE '
    CREATE TABLE comments (
      id VARCHAR2(36) PRIMARY KEY,
      post_id VARCHAR2(36),
      author_id VARCHAR2(50),
      content CLOB,
      created_at VARCHAR2(50)
    )'
; EXCEPTION WHEN OTHERS THEN NULL; END;

-- Note: adjust privileges and run as a DBA if needed.

SELECT * FROM COMMENTS c ;
