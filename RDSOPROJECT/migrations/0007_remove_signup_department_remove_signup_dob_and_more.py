# Generated by Django 4.2.2 on 2023-06-25 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rdsoproject', '0006_alter_signup_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='department',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='phone',
        ),
    ]
