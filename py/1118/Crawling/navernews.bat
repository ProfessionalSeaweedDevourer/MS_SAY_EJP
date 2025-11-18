@echo off
REM First Script
echo 1. Crawling and DB Insertion...
python "p02_navernews.py"

REM Second Script
echo 2. DB to TXT Conversion...
python "p03_navernewsintotxt.py"

echo Completed all tasks.
pause