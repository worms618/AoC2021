@ECHO OFF
SET DAYNR=1
SET DAY=day%DAYNR%

CALL python ..\src\%DAY%\%DAY%.py
PAUSE