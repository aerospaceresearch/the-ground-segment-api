# Generated by Django 2.0.6 on 2018-06-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='token',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]