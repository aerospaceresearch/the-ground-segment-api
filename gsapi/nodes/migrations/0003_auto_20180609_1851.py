# Generated by Django 2.0.6 on 2018-06-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0002_auto_20180609_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='token',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
