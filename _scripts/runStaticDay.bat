@ECHO OFF
SET DAYNR=18
SET DAYROOT=..\src
SET DAY=day%DAYNR%

CALL python %DAYROOT%\%DAY%\%DAY%.py
PAUSE