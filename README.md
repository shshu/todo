# run inside docker postres

1. docker-compose up
2. Run inside docker
    2.1 docker exec -it backend_postgres psql -U postgres
    2.2 create database backend;
3. python backend/manage.py db init
4. python backend/manage.py db migrate
5. python backend/manage.py db upgrade
