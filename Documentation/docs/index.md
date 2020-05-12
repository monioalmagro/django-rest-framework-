# DJANGO REST FRAMEWORK


## Usuario
- user = admin
- email = admin@admin.com    
- password = admin    

## Creamos el proyecto rest 

- django-admin startproject rest

##  Instalamos en el entorno el framework

- pip install djangorestframework

## Instalamos en app el framework
 
- en rest/rest/settings.py
  INSTALLED APPS:
  agregamos 'rest_framework',

## Creamos la app api

- creamos la app api
python manage.py startapp api

## Registramos la app

- En INSTALLED APPS:
'api',

## Creamos los archivos serializers.py y api.py

- serializers similar a models y api similar a views

- en api/
agregamos serializers.py (convierte json en dic y viseversa)

- en api/
creamos otro archivo api.py

## agregamos la ruta

- en  rest/rest/urls.py
creamos la ruta

## Migramos

- Make migration and Migrate

 

