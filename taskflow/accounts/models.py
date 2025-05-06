from django.db import models
from django.contrib.auth.models import AbstractUser
from taskflow.core.models.audition import AuditableModel

# Create your models here.


class UserAccount(AbstractUser, AuditableModel):

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=300)
