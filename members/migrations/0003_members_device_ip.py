# Generated by Django 4.1.3 on 2022-11-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_status_members_is_connected'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='device_ip',
            field=models.GenericIPAddressField(default='0.0.0.0'),
        ),
    ]