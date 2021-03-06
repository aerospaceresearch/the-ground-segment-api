# Generated by Django 2.0.6 on 2018-06-12 19:28

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import nodes.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0003_auto_20180609_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('upload', models.FileField(blank=True, max_length=254, null=True, upload_to=nodes.models.upload_directory)),
                ('upload_type', models.CharField(default='recording', max_length=255)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterModelOptions(
            name='node',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Status'},
        ),
        migrations.AddField(
            model_name='upload',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodes.Node'),
        ),
    ]
