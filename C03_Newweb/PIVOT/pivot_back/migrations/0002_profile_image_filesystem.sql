-- Migration: move profile image storage to filesystem
-- Adds filename/mime columns and drops binary column if present

ALTER TABLE users ADD (
  profile_image_filename VARCHAR2(255),
  profile_image_mime VARCHAR2(100)
);

-- If a previous column `profile_image` (BLOB) exists and you want to drop it, run the following (careful: irreversible):
-- ALTER TABLE users DROP COLUMN profile_image;

-- Note: For Oracle, dropping columns may require different privileges; run this in a maintenance window if needed.
