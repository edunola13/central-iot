# Hibris IOT Core Api

## Dependencies
Only run in Linux
 - Python 3
 - Redis

## Initial Steps
- Clone repo
- Create (virtualenv env --python=python3) and activate (source env/bin/activate) virtual env
- Install requeriment (pip): pip install -r requirements.txt
- Create database (IOT_DB)

## Local Settings (DEVELOPMENT)
```
(env) $ cp hibris_iot/local_settings.example.py hibris_iot/local_settings.py
(env) $ cp hibris_iot/secrets.example.py hibris_iot/secrets.py
Configure Celery "Broker"
```
The most important configurations are:
- DATABASES: Database configuration
- CELERY_*: Celery configuration
- SITE_URL
- All configs and keys of external services

## Environment Variables (PRODUCTION)
Create hibris_iot/.env variables or set the environment variables.
Use like example hibris_iot/.env.example
https://django-environ.readthedocs.io/en/latest/

## Migrations
```
(env) $ python manage.py makemigrations ---> Not run in Prod
(env) $ python manage.py migrate --database=default
```

## Translates
Generate the .po files `python manage.py makemessages --locale=es --locale=es_AR --extension=py --ignore=env/*`. Add more locales.
Change the .po files with the new keys.
After that we compile: `python manage.py compilemessages`

## Static Files
In production. When DEBUG=False it is necessary compile the static files. This is because django dont manage this, you need to pass to nginx for example.
Set in settings:
STATIC_ROOT = "/var/www/example.com/static/" -< When compile store there

Run the command:
`(env) $ python manage.py collectstatic`

Notes: https://docs.djangoproject.com/en/2.2/howto/static-files/deployment/#serving-static-files-from-a-dedicated-server

## Django Extensions
The lib 'django-extensions' provide utils functions. For example we can see the all urls and your reverse names.

Add in installed_apps -> 'django_extensions'

`(env) $ pip install django-extensions`
`(env) $ python manage.py show_urls`

## Run Server API
`(env) $ python manage.py runserver 0.0.0.0:port`

## Run Celery "Broker": Redis
`$ redis-server`
It's not necessary run in the root folder of the app. This is globally. https://redis.io/download

## Run Celery (DEV)
`(env) $ celery -A hibris_iot worker -l info -B`

## Run Celery (PROD)
`(env) $ celery -A hibris_iot worker -l info`
`(env) $ celery -A hibris_iot beat -l info`

## Run diferents workers
`(env) $ python main.py {worker}`
workers:
- iot_listener_mqtt 

## Run tests with coverage
`(env) $ coverage run --omit=env/* manage.py test`
`(env) $ coverage html`
Actual Coverage: 0%

## Dockers

### Build
Dockerfiles are located in dockers. We have one Dockerfile for all the entrypoints.
In the entrypoint are defined all the posibilities.

sudo docker build -t hibris_iot . -f dockers/Dockerfile

### Run
sudo docker run -p 8000:8000 --env-file hibris_iot/.env hibris_iot {action}

add "-d" to run in background

### Docker Compose
Move to /dockers folder and run
docker-compose pull && docker-compose up

### Docker Monitor
sudo docker stats ===>>> Monitorea los contenedores corriendo
sudo docker exec -it ID_CONTAINER bash ===>>> Entrar al container
sudo docker exec -it 564600ef2b7b /bin/sh ===>>> Entrar al container
ifconfig ===>>> Info de Red
docker logs ID_CONTAINER ===>>> Ver log

# Configure Oauth2

## Create User
```
from django_module_users.models import User 
User.create("edu", "edu@bn.com", "1234", True)
```

# Documentation

## Swagger
Swagger are available in /swagger only for Debug=True.
For access to definition of swagger you need to get the url: http://localhost:8001/swagger.json with credentials. This is with the header Authorization.

In http://localhost:8001/swagger.json or http://localhost:8001/swagger/?format=openapi you can download the json and next open in https://editor.swagger.io/

Notes: https://drf-yasg.readthedocs.io/en/latest/readme.html, https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#infoObject

In the root folder the file "swagger-file" with last json.

## Postman
In the root folder the file "hibris_iot.postman_collection.json" is the last collection.

For use need an environment with next variabled:
 - URL: Define for example http://localhost:8000. No "/" to the end.
 - TOKEN: Dont set anything.
