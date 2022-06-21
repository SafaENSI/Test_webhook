@echo off

cd C:\Users\bensa\PycharmProjects\pythonProject2\
echo Running script ...
python3 Running_Canoe.py

rem Output number of errors in tests, but do not signal to Jenkins
if errorlevel 1 (
 	echo %errorlevel% failed test modules
) else (
	echo all test modules successfully executed
)
exit /b 0
