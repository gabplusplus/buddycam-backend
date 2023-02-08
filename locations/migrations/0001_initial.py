# Generated by Django 4.1.3 on 2023-02-08 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0011_remove_devices_lat_remove_devices_long'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('device_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='location_id', serialize=False, to='devices.devices')),
                ('lat', models.FloatField(default=0)),
                ('long', models.FloatField(default=0)),
            ],
        ),
    ]