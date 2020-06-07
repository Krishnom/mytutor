rm db.sqlite3
find app -type d -name "__pycache__" -exec rm -r {} \;
find mytutor  -type d -name "__pycache__" -exec rm -r {} \;
find app -type d -name "migrations" -exec rm -r {} \;
