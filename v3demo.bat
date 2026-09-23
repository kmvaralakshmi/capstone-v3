@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    echo Project virtual environment not found.
    echo Run setup_windows.bat first.
    pause
    exit /b 1
)

set "V3_ARGS=%*"
".venv\Scripts\python.exe" v3demo.py %V3_ARGS%
pause