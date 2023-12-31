# Generated by Django 4.1.3 on 2023-01-31 18:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_devices_lat_devices_long'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='devices',
            name='device_ip',
            field=models.CharField(max_length=255),
        ),
    ]
