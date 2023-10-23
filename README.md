# teams-people-api

Python project for creating teams and people and assigning people to teams

## Features

- Full CRUD for Team model
- Full CRUD for People model
- Assigning Team for every person from People
- Assigning People for Team model

## Technologies used

Django REST Framework, PostgreSQL, SQLite, Docker, Docker-compose

## How to run

### Using Docker

- Docker already must be installed
- Clone this repo:
```shell
git clone https://github.com/ant-komarov/teams-people-api.git
cd teams-people-api
```
- Create ```.env``` file with data from ```.env.sample``` file:
    
    - ```DJANGO_SECRET_KEY``` you can generate at [djecrety.ir](https://djecrety.ir/);

    - ```DJANGO_DB=postgres``` for using PostgreSQL 
- In ```bush``` console input:
```shell
docker-compose up --build
```

### Shutdown

```CTRL + C```

### Run without Docker

- Clone this repo:
```shell
git clone https://github.com/ant-komarov/teams-people-api.git
cd teams-people-api
# for Windows:
python -m venv venv
venv\Scripts\activate
# for Mac and Linux:
python3 -m venv venv
source venv/bin/activate
```
- Create ```.env``` file with data from ```.env.sample``` file:
    
    - ```DJANGO_SECRET_KEY``` you can generate at [djecrety.ir](https://djecrety.ir/);

    - ```DJANGO_DB=default``` or delete this variable from file for using sqlite3
- In terminal input:
```shell
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
You can fill database with prepare data from fixture:
```shell
python manage.py loaddata teams_people_data.json
```

### For running tests:

Added tests only for custom logic

```shell
python manage.py test
```

## Documentation

- Swagger documentation available at: ```/api/doc/swagger/```
- Redoc documentation available at : ```api/doc/redoc/```
