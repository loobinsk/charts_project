# Generated by Django 2.2.10 on 2021-05-12 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0018_auto_20210512_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='image',
        ),
    ]
