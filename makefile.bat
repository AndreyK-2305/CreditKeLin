@echo off
REM Simula un Makefile con varias reglas en un archivo batch

if "%1" == "requirements" goto setup
if "%1" == "lint" goto lint
if "%1" == "test" goto test
if "%1" == "run" goto run
if "%1" == "migrate" goto migrate
if "%1" == "help" goto help
goto end



:setup
pip install -r requirements.txt
goto end

:lint
ruff format .
goto end

:test
coverage run manage.py test
coverage report -m
goto end

:run
python manage.py runserver --settings=creditkelin.settings.local
goto end

:migrate
python manage.py makemigrations
python manage.py migrate
goto end

:help
echo Available Commands:
echo requirements      Create and activate the Virtual environment, and install dependencies
echo lint       Format python files
echo test       Run Django tests
echo run        Run Django server
echo migrate    Apply modifications to Database
goto end

:end
