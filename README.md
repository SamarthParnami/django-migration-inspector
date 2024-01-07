# Django-Migration-Inspector

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Django-Migration-Inspector is a Python package that allows you to validate Django migrations in the command line. 

## Features

- Validates whether Django migration files refer to valid files when defining dependencies or run-after.
- Validates the dependency graph of the migration tree.
- Ensured that migration history for the project on DB is linear.
- Easy to integrate into your Django project.

## Installation

You can install Django-Migration-Inspector using pip:

```bash
pip install django-migration-inspector
```

## Usage
Add `inspector` to the INSTALLED_APPS inside the Django settings.


To use Django-Migration-Inspector, run the following command in your Django project:

```bash
python manage.py inspectmigrations
```
To run all the migration checks.


```bash
python manage.py inspectmigrations --skip-history-check
```
To skip the validation of applied migrations add flag `--skip-history-check`.


```bash
python manage.py inspectmigrations --database=alias
```
Optionally you can provide the alias for the configured database in the Django settings under `DATABASES`.
This ensures that inspection for the consistency of the already applied migrations is run from that particular Database.

## Support and Issues
For bug reports, feature requests, or general questions, please use the [GitHub Issues](https://github.com/SamarthParnami/django-migration-inspector/issues).