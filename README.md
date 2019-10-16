# Djynamic

Example implementation app of django-dynamic-admin for **Django admin**.

Current development version includes an example bundle and taxonomy.

(https://code.djangoproject.com/wiki/DynamicModels)

## Installing (Linux)
```
virtualenv -p /usr/bin/python3 env
source env/bin/activate
pip install -r requirements.txt
python src/manage.py migrate
python src/manage.py createsuperuser
python src/manage.py collectstatic
python src/manage.py runserver
```

## Setting up

(Rename `settings_example.py` to `settings.py`)

```
INSTALLED_APPS = [
    'djynamic.entity',
    'djynamic.taxonomy',
    'djynamic.bundle',
    'djynamic.example_bundle',
    'djynamic.example_bundle.example_content_models',
]
```

## Using
1. Use Django administration (http://127.0.0.1:8000/admin/) to;
2. Create a bundle content type through the `ExampleBundle` model provided adding any fields.
3. Optionally create taxonomy dictionaries and add a taxonomy dictionary field.
4. `makemigrations; migrate`
5. And voila!
