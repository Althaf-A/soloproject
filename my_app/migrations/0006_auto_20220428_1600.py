# Generated by Django 3.1.5 on 2022-04-28 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_feedback_worker_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='work_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='user_register',
            name='work_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wrname', to='my_app.work_name'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='work_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wrkname', to='my_app.work_name'),
        ),
        migrations.AlterField(
            model_name='work_details',
            name='work_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wrkename', to='my_app.work_name'),
        ),
    ]
