# Generated by Django 3.1.5 on 2022-04-27 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20220427_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_register',
            old_name='deptmnt',
            new_name='category',
        ),
    ]
