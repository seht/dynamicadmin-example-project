## Example implementation app of django-dynamic-admin

Includes an example bundle and taxonomy dictionary.

(https://code.djangoproject.com/wiki/DynamicModels)

## Installing (Linux)
```
virtualenv -p /usr/bin/python3 env
source env/bin/activate
pip install -r requirements.txt
python mysite/manage.py migrate
python mysite/manage.py makemigrations
python mysite/manage.py migrate
python mysite/manage.py createsuperuser
python mysite/manage.py collectstatic
python mysite/manage.py runserver
```

## Setting up

(Update settings in `settings.py`)

```
INSTALLED_APPS = [
    'polymorphic',
    'dynamicadmin',
    'example_bundle',
    'example_bundle.example_dynamic_models',
]
```

## Using
1. Use Django administration (http://127.0.0.1:8000/admin/) to;
2. Create a bundle content type through the `ExampleBundle` model provided and adding any fields.
3. Optionally create a taxonomy dictionary and add a taxonomy dictionary field.
4. Run `python src/manage.py makemigrations; python src/manage.py migrate`
5. Your new content types are available from (http://127.0.0.1:8000/admin/).

After making changes or adding more content types don't forget to run `python src/manage.py makemigrations; python src/manage.py migrate` when using Django admin.

(At some point a feature bypassing this step will be included in production.)

