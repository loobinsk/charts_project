# Generated by Django 2.2.10 on 2021-05-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='group',
            field=models.IntegerField(choices=[(0, 'worker'), (1, 'head of deportament')], max_length=255),
        ),
    ]