# Generated by Django 2.2.10 on 2021-05-10 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0013_testdata_teamleader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamleader',
            name='profile',
        ),
    ]