# Generated by Django 4.1.3 on 2023-02-04 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0008_alter_streams_device_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streams',
            name='switch',
        ),
    ]