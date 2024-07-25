@echo off
REM Batch script to encrypt a file using GPG

REM Define variables
SET RECIPIENT=kibitsuji@chef.com
SET INPUT_FILE=db.sqlite3
SET OUTPUT_FILE=fused

REM Check if GPG is installed
gpg --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo GPG is not installed or not in the PATH. Please install GPG.
    exit /b 1
)

REM Encrypt the file
gpg -r %RECIPIENT% -o %OUTPUT_FILE% -e %INPUT_FILE%

REM Check if the encryption was successful
IF ERRORLEVEL 1 (
    echo Encryption failed.
    exit /b 1
) ELSE (
    echo Encryption successful. Encrypted file saved as %OUTPUT_FILE%.
)