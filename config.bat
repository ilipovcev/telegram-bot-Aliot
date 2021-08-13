@echo off
chcp 1252>NUL

set /p TOKEN=Enter Telegram API Token: 

echo. 2>"config.py"

SETLOCAL ENABLEDELAYEDEXPANSION
for /f "delims=" %%L in ('type default-config.py') DO (
    SET "line=%%L"
    set "nline=!line:<TOKEN>=%TOKEN%!"
    echo !nline!>>"config.py"
    echo !nline!
    echo !line!
)
ENDLOCAL
