# Generated by Django 4.1.3 on 2023-02-11 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0014_alter_streams_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streams',
            name='status',
        ),
    ]