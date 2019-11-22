@echo off
set PATH=%PATH%;"C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\x64"
SET WORKING_DIR=%cd%
makecert.exe -a sha1 -r -pe -ss my -n "CN=VirtualBoxSHA1" %WORKING_DIR%\testcert_1.cer
makecert.exe -a sha256 -r -pe -ss my -n "CN=VirtualBoxSHA256" %WORKING_DIR%\testcert_256.cer
certmgr.exe -add %WORKING_DIR%\testcert_1.cer -s -r localMachine root
certmgr.exe -add %WORKING_DIR%\testcert_256.cer -s -r localMachine root

