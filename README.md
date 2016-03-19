#TREC Evaluator

This is a django webapp to perform search comparison magic

##Steps to setup

1. mkvirtualenv --system-site-packages <env_name>

2. pip install -U django==1.7.11
   pip install django-registration-redux

3. In a directory, call git clone https://github.com/gaftra/trec_evalutor.git. This will create a folder structure of trec_evalutor/<repo_contents>

4. Create a database superuser via python manage.py createsuperuser

5. Create a test database using python manage.py migrate and python populate_trecapp.py

6. run python manage.py runserver, and navigate to 127.0.0.1:8000/trecapp

##Contributors
----------------------------
gaftra: Stephen Brown 1106679B
juranec: Daniel Juranec 2145171J
kristinagenova: Kristina Genova <number>
<githubID>: Dominykas Vytautas Jakstonis <number>
