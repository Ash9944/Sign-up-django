# Generated by Django 3.2.6 on 2021-11-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='member',
            name='password',
        ),
        migrations.RemoveField(
            model_name='member',
            name='username',
        ),
        migrations.AddField(
            model_name='member',
            name='Address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='Email',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='Name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='Password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='Username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
