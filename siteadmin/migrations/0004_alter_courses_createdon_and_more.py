# Generated by Django 4.0.1 on 2022-02-19 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0003_alter_courses_createdon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 23, 23, 35, 837206)),
        ),
        migrations.AlterField(
            model_name='subtopiccontent',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 23, 23, 35, 838223)),
        ),
        migrations.AlterField(
            model_name='subtopics',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 23, 23, 35, 838223)),
        ),
        migrations.AlterField(
            model_name='units',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 23, 23, 35, 838223)),
        ),
    ]
