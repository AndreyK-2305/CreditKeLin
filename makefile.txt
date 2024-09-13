
# Variables
VENV = venv
PYTHON = (VENV)\Scripts\python.exe
PIP = (VENV)\Scripts\pip.exe
REQS = requirements.txt

# Rules
venv:
	python -m venv VENV

install: venv
	PIP install -r REQS

run: venv
	PYTHON manage.py runserver

migrate: venv
	PYTHON manage.py migrate

makemigrations: venv
	PYTHON manage.py makemigrations

createsuperuser: venv
	PYTHON manage.py createsuperuser

clean:
	rmdir /s /q __pycache__ VENV
