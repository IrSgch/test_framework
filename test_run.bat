@echo off
cd /d "C:\test_framework"
call venv\Scripts\activate.bat
python -m pytest -s -v
pause