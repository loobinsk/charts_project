# Generated by Django 2.2.10 on 2021-05-03 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data1', models.IntegerField()),
                ('data2', models.IntegerField()),
                ('data3', models.IntegerField()),
                ('data4', models.IntegerField()),
                ('data5', models.IntegerField()),
                ('date', models.DateField()),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'информация',
                'verbose_name_plural': 'инофрмации',
            },
        ),
    ]
