# Generated by Django 3.2.6 on 2021-08-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0004_alter_person_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.IntegerField(),
        ),
    ]