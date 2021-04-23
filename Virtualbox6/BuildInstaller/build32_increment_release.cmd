@echo off

title build Virtualbox Additions x86

cd /d %~dp0
for /f "tokens=3" %%i in ('findstr /B /R /C:"VBOX_VERSION_MAJOR *=" Version.kmk') do SET VBOX_VER_MJ=%%i
for /f "tokens=3" %%i in ('findstr /B /R /C:"VBOX_VERSION_MINOR *=" Version.kmk') do SET VBOX_VER_MN=%%i
for /f "tokens=3" %%i in ('findstr /B /R /C:"VBOX_VERSION_BUILD *=" Version.kmk') do SET VBOX_VER_BLD=%%i
for /f "tokens=6" %%i in ('findstr /C:"$Rev: " Config.kmk') do SET VBOX_REV=%%i
for /f "tokens=3" %%i in ('findstr /B /C:"VBOX_BUILD_PUBLISHER :=" LocalConfig.kmk') do SET VBOX_VER_PUB=%%i

set VERSION=%VBOX_VER_MJ%.%VBOX_VER_MN%.%VBOX_VER_BLD%%VBOX_VER_PUB%-r%VBOX_REV%
set VBOX_VER_MJ=
set VBOX_VER_MN=
set VBOX_VER_BLD=
set VBOX_VER_PUB=

echo "INSTALLER CONFIGURATION"

call "C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.Cmd" /Release /x86 /win7
REM TODO: try it also
REM call C:\MSVS\10.0\VC\bin\vcvars32.bat

if ERRORLEVEL 1 exit /b 1

set KBUILD_TARGET_ARCH=x86
set BUILD_TARGET_ARCH=x86
set PATH=%PATH%;%~dp0kBuild\bin\win.x86;%~dp0tools\win.x86\bin;C:\lib\mingw\mingw32\bin;C:\Python27

cscript configure.vbs --target-arch=x86 --with-vc="C:\MSVS\10.0\VC" --with-DDK=C:\WinDDK\7600.16385.1 --with-w32api=c:\lib\mingw\mingw32 --with-MinGW-w64=C:\lib\mingw\mingw64 --with-MinGW32=C:\lib\mingw\mingw32 --with-libSDL=C:\lib\SDL\x86\SDL-1.2.15 --with-openssl=C:\lib\OpenSSL\x32 --with-libcurl=C:\lib\curl\x86 --with-Qt5=C:\Qt\5.6.3\msvc2010 --with-libvpx=C:\lib\libvpx --with-libopus=C:\lib\libopus --with-python=C:/Python27
if ERRORLEVEL 1 exit /b 1

call env.bat
if ERRORLEVEL 1 exit /b 1

REM Commands for verbose output
REM kmk --pretty-command-printing --jobs=1
REM kmk --debug=vjm KBUILD_TYPE=debug
kmk

if ERRORLEVEL 1 exit /b 1

del /q AutoConfig.kmk configure.log env.bat
