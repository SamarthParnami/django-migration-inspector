# Django-Migration-Inspector

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Django-Migration-Inspector is a Python package that allows you to validate Django migrations in the command line. 

## Features

- Validates whether Django migration files refer to valid files when defining dependencies or run-after.
- Validates the depdency graph of the migration tree.
- Ensured that migration history for the prjoect on DB is linear.
- Easy to integrate into your Django project.

## Installation

You can install Django-Migration-Inspector using pip:

```bash
pip install django-migration-inspector
```

## Usage
To use Django-Migration-Inspector, run the following command in your Django project:

!! You must configure `INSPECTOR_DATABASES` in settings with nested dictionary conataining the options for an individual database.
```python
INSPECTOR_DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

```bash
python manage.py inspectmigrations
```
To run all the migration checks including the migration history validation on the 'default' database.


```bash
python manage.py inspectmigrations --skip-history-check
```
Skips the validation of applied migrations.

## Support and Issues
For bug reports, feature requests, or general questions, please use the [GitHub Issues](https://github.com/SamarthParnami/django-migration-inspector/issues).