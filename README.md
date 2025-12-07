# Django Starter Project

This minimal Django project serves as a starting point to build on.

## Setup

From PowerShell:

```powershell
# Create a virtual environment
C:/Users/AndiS/AppData/Local/Programs/Python/Python313/python.exe -m venv venv

# Activate
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Apply migrations and run server
python manage.py migrate
python manage.py runserver
```

## Create a superuser

```powershell
python manage.py createsuperuser
```

## Test

```powershell
python manage.py test
```

## Notes
- This uses SQLite by default.
- Update `mysite/settings.py` for production settings.
