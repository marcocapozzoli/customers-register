# Generated by Django 3.2.6 on 2021-08-16 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0009_alter_person_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='social_media',
            field=models.URLField(null=True),
        ),
    ]