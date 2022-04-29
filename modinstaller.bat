@echo off
CLS
:init
setlocal DisableDelayedExpansion
set "batchPath=%~0"
for %%k in (%0) do set batchName=%%~nk
set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
setlocal EnableDelayedExpansion

:checkPrivileges
NET FILE 1>NUL 2>NUL
if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )

:getPrivileges
if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)

ECHO Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
ECHO args = "ELEV " >> "%vbsGetPrivileges%"
ECHO For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
ECHO args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
ECHO Next >> "%vbsGetPrivileges%"
ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
"%SystemRoot%\System32\WScript.exe" "%vbsGetPrivileges%" %*
exit /B
exit
:gotPrivileges
setlocal & pushd .
cd /d %~dp0
if '%1'=='ELEV' (del "%vbsGetPrivileges%" 1>nul 2>nul  &  shift /1)

::start
if exist pythoninstaller.bat del pythoninstaller.bat
python --version >nul 2>&1 && ( goto gotpy ) || ( goto install )


:install
echo Python missing, installing now.
curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/pythoninstaller.bat -O
pythoninstaller.bat
exit





:gotpy
pip install requests --quiet
pip install progressbar2 --quiet
set scriptpath=%~dp0
c:
cd %appdata%
cd .minecraft
if not exist mods mkdir mods
cd mods
if exist modinstaller-files rmdir /Q /S modinstaller-files 
mkdir modinstaller-files
cd modinstaller-files && if not exist updater.py curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/updater.py -O
curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/urls.txt -O
curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/installer.py -O
python modinstaller-files/updater.py %scriptpath%
python installer.py
del urls.txt
del installer.py
