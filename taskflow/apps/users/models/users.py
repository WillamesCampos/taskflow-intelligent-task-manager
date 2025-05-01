from django.db import models
from django.contrib.auth.models import AbstractUser
from taskflow.apps.core.models.audition import AuditableModel

# Create your models here.


class User(AbstractUser, AuditableModel):

    id = models.AutoField()
    first_name = models.Charfield(max_lenght=80)
    last_name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)