@ECHO OFF
SET DAYNR=12
SET DAYROOT=..\src
SET SCRIPTSROOT=..\scripts
SET CREATEDAYSCRIPT=createDay.py

CALL python %SCRIPTSROOT%\%CREATEDAYSCRIPT% %DAYROOT% %DAYNR%
PAUSE