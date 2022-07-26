from django.db import models
from user.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = 'note'
