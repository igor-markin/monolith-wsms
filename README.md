# Web Servers Monitoring System
A system that enable health monitoring of web servers in the cloud.

## How to run the project
- Install Docker and Docker Compose
- Clone this project to your computer
- From the project directory, execute the command `docker compose build && docker compose up`
- Create superuser with `docker compose exec web python manage.py createsuperuser`
- Load database dump with `docker compose exec web python manage.py loaddata dump.json`
- Open the admin panel and check that everything works http://localhost/admin/

## Stack of technologies used in the project

- Python
- Django
- Rest Framework
- PostgreSQL
- Redis
- Nginx
- Celery
- Docker Compose

## API Documentation
- http://localhost/api/swagger/
- http://localhost/api/redoc/