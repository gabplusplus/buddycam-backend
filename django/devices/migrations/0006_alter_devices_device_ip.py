# Generated by Django 4.1.3 on 2023-01-29 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_devices_lat_devices_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='device_ip',
            field=models.URLField(primary_key=True, serialize=False),
        ),
    ]
