# Generated by Django 3.0.3 on 2020-09-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200913_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_content',
            field=models.TextField(default='these are the contents', max_length=1000),
        ),
    ]
