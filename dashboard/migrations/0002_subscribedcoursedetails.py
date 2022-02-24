# Generated by Django 4.0.2 on 2022-02-19 17:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('siteadmin', '0002_alter_courses_createdon_and_more'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribedCourseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('subscribedOn', models.DateTimeField(default=datetime.datetime(2022, 2, 19, 22, 41, 20, 98913))),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]