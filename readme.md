# django-starter-toolkit #


## How to use? ##

### Set up virtual python environment

Linux 64-bit

#### Python 3
$ sudo apt-get install python3-pip python3-dev python3-virtualenv

Mac OS X

$ sudo easy_install pip
$ sudo pip install --upgrade virtualenv

More on virtualenv ([http://docs.python-guide.org/en/latest/dev/virtualenvs/])

### Activate virtual environment and install django 1.10

    pip install django==1.10

To create a new Django project (make sure to change `test_project`)

    django-admin.py startproject --template=https://github.com/sijanonly/django-toolkit/archive/master.zip test_project

cd to your project and install the dependences

    pip install -r requirements.txt

If you need a database, edit the settings and create one with
   
    python manage.py migrate

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    python manage.py runserver


Feel free to contribute.[# How to contribute to a project ?](https://guides.github.com/activities/contributing-to-open-source/#contributing target="_blank")
<a href="https://guides.github.com/activities/contributing-to-open-source/#contributing" target="_blank"># How to contribute to a project ?</a>