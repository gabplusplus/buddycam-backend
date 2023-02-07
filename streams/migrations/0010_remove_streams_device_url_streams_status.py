# Generated by Django 4.1.3 on 2023-02-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0009_remove_streams_switch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streams',
            name='device_url',
        ),
        migrations.AddField(
            model_name='streams',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
