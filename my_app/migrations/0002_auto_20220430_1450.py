# Generated by Django 3.1.5 on 2022-04-30 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(default='', max_length=300)),
                ('from_date', models.DateField(default='')),
                ('to_date', models.DateField(default='')),
                ('post_date', models.DateField(default='')),
                ('replay_date', models.DateField(default='')),
                ('feedback', models.CharField(max_length=300)),
                ('feedback_replay', models.CharField(max_length=300)),
                ('replay_status', models.CharField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('regdate', models.DateField(default='')),
                ('status', models.CharField(default='0', max_length=20)),
                ('photo', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='work_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.CharField(default='', max_length=200)),
                ('work_status', models.CharField(default='0', max_length=20)),
                ('work_city', models.CharField(default='', max_length=100)),
                ('experience', models.CharField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='work_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='work_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='login',
            name='designation',
        ),
        migrations.RenameModel(
            old_name='department',
            new_name='category',
        ),
        migrations.DeleteModel(
            name='candidates',
        ),
        migrations.DeleteModel(
            name='designation',
        ),
        migrations.DeleteModel(
            name='login',
        ),
        migrations.AddField(
            model_name='work_details',
            name='category_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worker_dep', to='my_app.category'),
        ),
        migrations.AddField(
            model_name='work_details',
            name='work_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wrkename', to='my_app.work_name'),
        ),
        migrations.AddField(
            model_name='work_details',
            name='work_type',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='desgn', to='my_app.work_type'),
        ),
        migrations.AddField(
            model_name='work_details',
            name='worker_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worker_id', to='my_app.user_register'),
        ),
        migrations.AddField(
            model_name='user_register',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dep', to='my_app.category'),
        ),
        migrations.AddField(
            model_name='user_register',
            name='work_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wrname', to='my_app.work_name'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='category_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin', to='my_app.category'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userid', to='my_app.user_register'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='work_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wrkname', to='my_app.work_name'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='work_type',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worktyp', to='my_app.work_type'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='worker_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worker1', to='my_app.user_register'),
        ),
    ]
