# API Backend

application for TODO list

## Python setup

1. python3 -m venv env
2. source env/bin/activate
3. pip install requirements.txt

## Postgres setup

1. docker-compose up
2. Run inside docker:
    2.1 docker exec -it backend_postgres psql -U postgres
    2.2 create database backend

## DB setup

1. python backend/manage.py db init
2. python backend/manage.py db migrate
3. python backend/manage.py db upgrade

## Run application (dev)

create .env file in root of the project

```python
SECRET_KEY=[your_secret]
JWT_SECRET_KEY=[your_secret]
```

```bash
export FLASK_ENV=development
export FLASK_APP=backend/app.py
flask run
```
