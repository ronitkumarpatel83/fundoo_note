# Generated by Django 4.0.6 on 2022-08-10 04:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_rename_notes_note_alter_note_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]