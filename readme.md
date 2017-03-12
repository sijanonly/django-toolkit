# django-starter-toolkit #


## How to use? ##

### Set up virtual python environment

Linux 64-bit

# Python 3
$ sudo apt-get install python3-pip python3-dev python3-virtualenv

Mac OS X

$ sudo easy_install pip
$ sudo pip install --upgrade virtualenv

More on virtualenv ([http://docs.python-guide.org/en/latest/dev/virtualenvs/])

### Activate virtual environment and install django 1.10

    pip install django==1.10

To create a new Django project (make sure to change `project_name`)

    django-admin.py startproject --template=https://github.com/fasouto/django-starter-template/archive/master.zip --extension=py,md,html,txt,less project_name

cd to your project and install the dependences

    pip install -r requirements.txt

If you need a database, edit the settings and create one with
   
    python manage.py migrate

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    python manage.py runserver

## How to use it ##

### Settings ###

Settings are divided by environments: production.py, development.py and testing.py. By default it uses development.py, if you want to change the environment set a environment variable:

    export DJANGO_SETTINGS_MODULE="my_project.settings.production"

or you can use the `settings` param with runserver:

    python manage.py runserver --settings=my_project.settings.production

If you need to add some settings that are specific for your machine, rename the file `local_example.py` to `local_settings.py`. This file it's in .gitignore so the changes won't be tracked.

