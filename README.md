``` bash
pip install django
django-admin startproject myproject
cd myproject
conda create -p venv python==3.11
conda activate venv/
pip install django
python manage.py startapp myapp 
# myapp is root app

# we create multiple  apps in the same project
##Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
##
git init
git add README.md 
git  commit -m "first commit"
git remote add origin https://github.com/SAMANTA1401/django_project.git
git push -u origin main
## create .gitignore file from github
git pull

## add myapp to myproject>settings>installed apps
## add urls.py to myapp
## include myapp.urls to myproject.urls

## create templates dir
## creaet static dir for static file
## add templates to settings.py>TEMPLATES>DIRS
# add static file to setting.py>STATICFILES_DIR	
```