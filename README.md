# NimapInfotech_MT
This  repo is for machine test provided by Nimap Infotech
steps for setup
1) clone MachineTest into your desired directory
2) nevigate to client_project
3) create a virtual enviornment by using python -m venv env
4) Activate env using .\env\Scripts\activate for windows
5) Activate env using source env\bin\activate for ubuntu
6) install requirements.txt using pip install -r requirements.txt
7) nevigate to client_project_system
8) go to settings.py add your sql database credentials
9) python manage.py makemigrations
10) python manage.py migrate
11) python manage.py runserver
12) for testing after runserver you can use postman , thunderclient or type http://127.0.0.1:8000/static/index.html
13) get token  from admin interface of django
14) test apis

    


