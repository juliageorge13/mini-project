# Generated by Django 4.0.2 on 2022-02-19 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0002_alter_courses_createdon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 22, 42, 43, 690547)),
        ),
        migrations.AlterField(
            model_name='subtopiccontent',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 22, 42, 43, 692542)),
        ),
        migrations.AlterField(
            model_name='subtopics',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 22, 42, 43, 691545)),
        ),
        migrations.AlterField(
            model_name='units',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 22, 42, 43, 691545)),
        ),
    ]
