# Generated by Django 2.2.10 on 2021-05-10 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0006_profile_head_of_deportment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='head_of_deportment',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='teamleader',
        ),
        migrations.CreateModel(
            name='TeamLeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='HeadOfDeportment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charts.Profile')),
            ],
        ),
    ]
