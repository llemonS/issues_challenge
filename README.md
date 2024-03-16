# Issues_challenge:
Challenge to develop a simple issue backend/frontend application.

## Stack:
- Django/DRF
- React

## Setup Steps:
1 - In order to run the project, one shall clone this repo and run:
```
docker-compose up --build
```
## Backend Testing:
If you want to run tests on backend:
```
docker-compose exec -it backend python manage.py test
```

## Project Structure:

 - Django Rest Framework:
 Issues can be posted directly on the URL `http://0.0.0.0:8000/api/issues/` if desired.
 - React Frontend:
 To perform CRUD with issues, access `http://0.0.0.0:3000`

## Definition of Done (DoD):
  - Attributes id, title, description, last_updated.
  - Backend (Django).
  - Frontend (React).
  - Containerized application.
