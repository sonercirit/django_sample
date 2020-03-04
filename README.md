# Sample Django App

## for local development

* create postgres database
```
docker-compose up -d
```
* change the db connection settings in `settings.py` file, if you are using docker-compose, they should be set up accordingly for local development
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
* install dependencies
```
pip install -r requirements.txt
```
* apply migrations
```
python manage.py migrate
```
* run app
```
python manage.py runserver
```
* access to the testing endpoint
```
http://127.0.0.1:8000/sample_app/last_points
```
### admin panel
* create user
```
python manage.py createsuperuser
```
* access panel
```
http://127.0.0.1:8000/admin
```