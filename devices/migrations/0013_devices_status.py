# Generated by Django 4.1.3 on 2023-02-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0012_devices_lat_devices_long'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='status',
            field=models.CharField(default='Disconnected', max_length=25),
        ),
    ]