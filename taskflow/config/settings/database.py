# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PG_DBNAME"),
        "USER": os.environ.get("PG_DBUSER"),
        "PASSWORD": os.environ.get("PG_DBPASSWORD"),
        "HOST": os.environ.get("PG_DBHOST"),
        "PORT": os.environ.get("PG_DBPORT")
    }
}
