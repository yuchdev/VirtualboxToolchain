@echo off

REM Remove certificates from LocalMachine/Root storage

set PATH=%PATH%;"C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\x64"
SET WORKING_DIR=%cd%

certmgr.exe -del -c -n "VirtualBoxSHA1" -s -r localMachine root
certmgr.exe -del -c -n "VirtualBoxSHA256" -s -r localMachine root
