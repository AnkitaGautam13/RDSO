# Generated by Django 4.2.2 on 2023-06-25 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rdsoproject', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='confirm_password',
        ),
    ]
