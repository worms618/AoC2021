@ECHO OFF
SET DAYNR=6
SET DAYROOT=..\src
SET DAY=day%DAYNR%

CALL python %DAYROOT%\%DAY%\%DAY%.py
PAUSE