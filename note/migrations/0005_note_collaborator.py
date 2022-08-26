# Generated by Django 4.0.6 on 2022-08-25 17:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0004_note_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='collaborator',
            field=models.ManyToManyField(related_name='collaborator', to=settings.AUTH_USER_MODEL),
        ),
    ]
