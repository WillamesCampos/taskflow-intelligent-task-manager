# Application definition
INSTALLED_APPS = []

PROJECT_APPS = [
    'taskflow.apps.accounts',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]


INSTALLED_APPS.extend(DJANGO_APPS)
INSTALLED_APPS.extend(PROJECT_APPS)
