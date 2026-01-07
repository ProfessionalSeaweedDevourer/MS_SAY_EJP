-- Migration: add profile columns to users table
-- Target DB: Oracle (VARCHAR2 types)

ALTER TABLE users ADD (
  name VARCHAR2(100),
  role VARCHAR2(100),
  description VARCHAR2(500)
);
