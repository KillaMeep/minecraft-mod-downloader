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
set scriptpath=%~dp0
set CUR_YYYY=%date:~10,4%
set CUR_MM=%date:~4,2%
set CUR_DD=%date:~7,2%
set CUR_HH=%time:~0,2%
if %CUR_HH% lss 10 (set CUR_HH=0%time:~1,1%)
set CUR_NN=%time:~3,2%
set CUR_SS=%time:~6,2%
set CUR_MS=%time:~9,2%
set SUBFILENAME=%CUR_YYYY%%CUR_MM%%CUR_DD%-%CUR_HH%%CUR_NN%%CUR_SS%
c:
cd %appdata%
cd .minecraft
if not exist mods mkdir mods
cd mods
if not exist modinstaller-files mkdir modinstaller-files
if exist *.jar mkdir mods-old-%SUBFILENAME% && copy *.jar mods-old-%SUBFILENAME% && del *.jar && cls
curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/urls.txt -O
curl -s https://raw.githubusercontent.com/KillaMeep/minecraft-mod-downloader/main/installer.py -O
python installer.py %scriptpath%
del urls.txt
del installer.py
