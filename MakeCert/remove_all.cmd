@echo off

REM Remove certificates from LocalMachine/Root storage

certmgr.exe -del -c -n "VirtualBoxSHA1" -s -r localMachine root
certmgr.exe -del -c -n "VirtualBoxSHA256" -s -r localMachine root
