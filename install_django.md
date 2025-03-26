All we need to setup a django server

## Start by installing python-pip

```bash
sudo apt-get install python3-pip
```

get virtual environment to work

```bash
sudo apt-get install python3-venv
```

## Create a new virtual environment inside project folder

### 1 create
```bash
python3 -m venv django-project-folder/venv
```

### 2 Check it exists

```bash
ls django-project-folder/
```
result:
```bash
blog djhango-project-name media requirements.txt venv 
db.sqlite3 manange.py users
```

### 3 go there

```bash
cd django-project-folder
```

### 4 Activate it

```bash
source venv/bin/activate 
```

Aqui está um setup eficiente para criar um ambiente virtual Python e instalar Django + Django REST Framework (DRF):  

## **2 Install dependencies**
```bash
pip install django djangorestframework
```
_if you haven't yet_

and the required packages:
```bash
pip install -r requirements.txt
```

## **3 Create the project

### 3.1. **Create a django project**  
```bash
django-admin startproject django_myproject_name
cd django_myproject_name
```

### 4. **Create an app Django for API**  
```bash
python manage.py startapp app_name
```

### 5. **Add DRF(django rest framework) to the project (`settings.py` file)**  

Edit `myproject/settings.py` and add `rest_framework` at `INSTALLED_APPS`:  

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'rest_framework', # this line here
    'api_name',  # your app, and this line too
]
```

### 6. **Execute migrations e boot up server**  

```bash
python manage.py migrate
python manage.py runserver
```
