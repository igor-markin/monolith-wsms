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
- To execute requests through Postman, you need to use the collection file `Main server.postman_collection.json`

## How to receive email notifications
- Add administrators and their mails to the ADMINS variable in the `django_inspector/django_inspector/settings.py`
- For convenience, letters are not sent for real yet, they are saved to files in the `/tmp/emails` directory

## Current problems of my solution:
- Low level of abstraction
- Unoptimized code
- Unoptimized database queries
- No tests
- No time zone dependency