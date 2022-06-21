cd C:\Users\bensa\PycharmProjects\pythonProject2\
python Running_Canoe.py

if errorlevel 1 (
 	echo %errorlevel% failed test modules
) else (
	echo all test modules successfully executed
)
exit /b 0
