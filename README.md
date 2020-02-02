# Django tree test task #

Used python 3.7 + Django 3.0 + sqllite3.


Package for install (Ubuntu 18.x) _build-essential, python3.7-venv, python3.7-dev, python3-venv


1. Create virtualenv:
python3.7 -m venv .env```
2. Set virtualenv
``` . ./.env/bin/activate```
3. Install requirements:
```
pip install --upgrade pip
pip install -r requirements.txt
```
4. Execution of migrations:
```
./manage.py migrate
```
6. Fixtures DB fill (if necessary)
```
./manage.py loaddata tree/fixtures/initial_data.json
```
7. Run test :
```
./manage.py test
```
8. run server
```
./manage.py runserver 127.0.0.1:8000
```

### http://127.0.0.1:8000/ - Get full tree ###
### http://127.0.0.1:8000/ - Get subtree by node id ###
### Code and main logic in   ###