@echo off
REM Change to the directory containing your Python script
cd /d C:\Users\jiang\Documents\GitHub\Shuochengwork

REM Use PyInstaller to compile the Python script to an executable
pyinstaller --onefile --noconsole Main_UI.py

REM Check if the build was successful
if %ERRORLEVEL% neq 0 (
    echo PyInstaller encountered an error.
    exit /b %ERRORLEVEL%
)

REM Define paths for the source and destination
set "source_dir=dist"
set "destination_dir=."
set "new_exe_name=Main_UI_Rev00.exe"
set "desktop_shortcut_name=Main_UI_Shortcut.lnk"

REM Move and rename the executable
echo Moving and renaming executable...
move /Y "%source_dir%\Main_UI.exe" "%destination_dir%\%new_exe_name%"

REM Check if the move was successful
if %ERRORLEVEL% neq 0 (
    echo Failed to move or rename the executable.
    exit /b %ERRORLEVEL%
)

REM Create a shortcut on the desktop
echo Creating shortcut on the desktop...
REM powershell -command "$s=(New-Object -COM WScript.Shell).CreateShortcut('$env:USERPROFILE\Desktop\%desktop_shortcut_name%'); $s.TargetPath='%cd%\%new_exe_name%'; $s.Save()"

REM Delete the build directory and other temporary files
echo Cleaning up build files...
rmdir /s /q build
REM rmdir /s /q dist
del /q Main_UI.spec

REM Optional: Pause to keep the command window open
pause