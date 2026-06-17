@echo off
REM ============================================================
REM  Ontwerpchecker - bouw een zelfstandige Windows .exe
REM  Dubbelklik dit bestand (of draai het in een opdrachtprompt)
REM  in de map waar ontwerpchecker.py / webapp.py staan.
REM
REM  Eenmalig is hiervoor Python nodig (om te bouwen). De .exe
REM  die eruit komt heeft GEEN Python nodig.
REM ============================================================
setlocal

where python >nul 2>nul
if errorlevel 1 (
  echo.
  echo Python is niet gevonden. Installeer Python 3.10+ van https://www.python.org/downloads/
  echo en vink "Add python.exe to PATH" aan. Of bouw de .exe via GitHub Actions
  echo zonder lokale Python ^(zie README, sectie "Bouwen zonder Python"^).
  echo.
  pause
  exit /b 1
)

echo [1/4] Virtuele omgeving aanmaken...
python -m venv build_env || goto :err
call build_env\Scripts\activate.bat || goto :err

echo [2/4] Pakketten installeren...
python -m pip install --upgrade pip >nul
pip install pyinstaller flask PyMuPDF openpyxl || goto :err

echo [3/4] Executable bouwen...
pyinstaller --noconfirm Ontwerpchecker.spec || goto :err

echo [4/4] Klaar.
echo.
echo De executable staat in:  dist\Ontwerpchecker.exe
echo Dubbelklik die om de tool te starten; je browser opent vanzelf.
echo.
pause
exit /b 0

:err
echo.
echo Er ging iets mis tijdens het bouwen. Lees de regels hierboven.
pause
exit /b 1
