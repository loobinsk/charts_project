# Generated by Django 2.2.10 on 2021-05-10 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0015_remove_headofdeportment_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamleader',
            name='HeadOfDeportment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='head_of_deportment', to='charts.HeadOfDeportment'),
        ),
    ]
