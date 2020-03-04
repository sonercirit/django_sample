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
* populate db for testing (first argument specifies the vehicle count while the other specifies navigation record count for each vehicle)
```
python manage.py populate 100 1000
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