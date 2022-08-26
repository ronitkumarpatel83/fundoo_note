from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = models.CharField(max_length=100, unique=True)
    # password = models.CharField(max_length=300)
    # first_name = models.CharField(max_length=100, null=True)
    # last_name = models.CharField(max_length=100, null=True)
    # email = models.EmailField(max_length=100, unique=True)
    phone_number = models.BigIntegerField()
    location = models.CharField(max_length=200)
    is_verify = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'


class Log(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    method = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'log'

