# Installation for windows

**Step 1** - *Project configurations*
```
git clone https://github.com/jdg24g/proyecto_grupal
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```
**Step 2** - *Django migrations*
```
python manage.py makemigrations
python manage.py migrate
```
**Step 3** - *Django admin panel credentials*
```
python manage.py createsuperuser
```
**Step 4** - *Run server*
```
python manage.py runserver
```

# Installation for linux

**Step 1** - *Project configurations*
```
git clone https://github.com/jdg24g/proyecto_grupal
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
**Step 2** - *Django migrations*
```
python3 manage.py makemigrations
python3 manage.py migrate
```
**Step 3** - *Django admin panel credentials*
```
python3 manage.py createsuperuser
```
**Step 4** - *Run server*
```
python3 manage.py runserver
```