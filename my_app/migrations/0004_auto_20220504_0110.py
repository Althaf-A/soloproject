# Generated by Django 3.1.5 on 2022-05-03 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20220504_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='work_type',
        ),
        migrations.RemoveField(
            model_name='user_register',
            name='work_type',
        ),
    ]
