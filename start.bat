@echo off
echo ============================================================
echo Plant Disease Detection System - Quick Start
echo ============================================================
echo.

:menu
echo Please select an option:
echo.
echo 1. Setup Environment (First Time)
echo 2. Download Dataset
echo 3. Start Jupyter Notebooks
echo 4. Start Backend Server
echo 5. Start Frontend Server
echo 6. Start Both Backend and Frontend
echo 7. Run Tests
echo 8. Exit
echo.

set /p choice="Enter your choice (1-8): "

if "%choice%"=="1" goto setup
if "%choice%"=="2" goto download
if "%choice%"=="3" goto jupyter
if "%choice%"=="4" goto backend
if "%choice%"=="5" goto frontend
if "%choice%"=="6" goto both
if "%choice%"=="7" goto test
if "%choice%"=="8" goto end
goto menu

:setup
echo.
echo Setting up environment...
echo.
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.
echo Setup complete!
echo.
pause
goto menu

:download
echo.
echo Downloading dataset...
echo Make sure Kaggle API is configured!
echo.
call venv\Scripts\activate
python download_data.py
echo.
pause
goto menu

:jupyter
echo.
echo Starting Jupyter Notebook...
echo.
call venv\Scripts\activate
jupyter notebook
goto menu

:backend
echo.
echo Starting Backend Server...
echo Backend will run at http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo.
call venv\Scripts\activate
cd backend
python app.py
cd ..
goto menu

:frontend
echo.
echo Starting Frontend Server...
echo Frontend will run at http://localhost:3000
echo.
call venv\Scripts\activate
python -m http.server 3000 --directory frontend
goto menu

:both
echo.
echo Starting Backend and Frontend...
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop servers
echo.
start cmd /k "cd /d %cd% && call venv\Scripts\activate && cd backend && python app.py"
timeout /t 5
start cmd /k "cd /d %cd% && call venv\Scripts\activate && python -m http.server 3000 --directory frontend"
start http://localhost:3000
goto menu

:test
echo.
echo Running tests...
echo.
call venv\Scripts\activate
echo Testing backend health...
curl http://localhost:8000/health
echo.
echo.
echo If you see an error, make sure backend is running!
echo.
pause
goto menu

:end
echo.
echo Thank you for using Plant Disease Detection System!
echo.
exit
