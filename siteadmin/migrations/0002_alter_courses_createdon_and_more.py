# Generated by Django 4.0.2 on 2022-02-19 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 22, 41, 20, 93948)),
        ),
        migrations.AlterField(
            model_name='subtopiccontent',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 22, 41, 20, 95918)),
        ),
        migrations.AlterField(
            model_name='subtopics',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 22, 41, 20, 95918)),
        ),
        migrations.AlterField(
            model_name='units',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 22, 41, 20, 94924)),
        ),
    ]