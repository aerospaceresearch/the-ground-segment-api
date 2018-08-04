# Generated by Django 2.0.8 on 2018-08-04 16:54

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0004_auto_20180612_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start', models.DateTimeField()),
                ('stop', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('default', models.BooleanField(default=False)),
                ('task', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodes.Node')),
            ],
            options={
                'verbose_name_plural': 'Jobs',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='upload',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodes.Job'),
        ),
    ]