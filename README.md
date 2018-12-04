# Django React Boilerplate

This repository contains a boilerplate project setup for Django and React. The project contains backend user authentication with the Django Rest Framework and rest-auth. The frontend has react redux sagas setup for user authentication in the frontend.

## Backend development workflow

```json
virtualenv env
pip install -r requirements.txt
cd src
python manage.py runserver
```

## Frontend development workflow

```json
cd frontend
npm i
npm start
```

## For deploying to Heroku

```json
npm run build
```