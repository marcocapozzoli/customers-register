# Generated by Django 3.2.6 on 2021-08-13 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
