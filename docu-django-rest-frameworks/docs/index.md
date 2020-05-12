# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Usuario
- user = admin
- email = admin@admin.com    
- password = admin    

## Creamos el proyecto rest 

- django-admin startproject rest

- en rest/rest/settings.py
 INSTALLED APPS:
 agregamos 'rest_framework',

- creamos la app api
python manage.py startapp api

. la registramos en INSTALLED APPS:
'api',

- serializers similar a models y api similar a views

- en api/
agregamos serializers.py (convierte json en dic y viseversa)

- en api/
creamos otro archivo api.py

- en  rest/rest/urls.py
creamos la ruta

- Make migration and Migrate

- levantamos el servidor 
-

