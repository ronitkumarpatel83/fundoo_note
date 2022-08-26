from django.db import models
from user.models import User
from datetime import datetime


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    collaborator = models.ManyToManyField(User, related_name='collaborator')
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'note'


