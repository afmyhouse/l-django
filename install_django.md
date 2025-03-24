Aqui está um setup eficiente para criar um ambiente virtual Python e instalar Django + Django REST Framework (DRF):  

### 1. **Criar e ativar um ambiente virtual**  
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows (cmd)
```

### 2. **Atualizar `pip` e instalar dependências**  
```bash
pip install --upgrade pip
pip install django djangorestframework
```

### 3. **Criar um projeto Django**  
```bash
django-admin startproject myproject
cd myproject
```

### 4. **Criar um app Django para API**  
```bash
python manage.py startapp api
```

### 5. **Adicionar DRF ao projeto (`settings.py`)**  
Edite `myproject/settings.py` e adicione `rest_framework` em `INSTALLED_APPS`:  
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'rest_framework',
    'api',  # Seu app
]
```

### 6. **Rodar as migrações e iniciar o servidor**  
```bash
python manage.py migrate
python manage.py runserver
```

Agora você tem um ambiente pronto com Django e DRF! 🚀  
Se precisar de autenticação, serializers ou views, só avisar.