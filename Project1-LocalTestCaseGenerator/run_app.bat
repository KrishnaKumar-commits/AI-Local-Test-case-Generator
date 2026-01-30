@echo off
cd /d "%~dp0"
echo Starting Local AI Test Case Generator...
cd backend
python main.py
pause
