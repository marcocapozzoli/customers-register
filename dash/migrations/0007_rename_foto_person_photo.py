# Generated by Django 3.2.6 on 2021-08-16 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0006_auto_20210815_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='foto',
            new_name='photo',
        ),
    ]
