# Generated by Django 4.0.6 on 2022-08-01 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
    ]
