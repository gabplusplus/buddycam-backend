# Generated by Django 4.1.3 on 2022-12-11 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_members_device_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='device_ip',
            field=models.GenericIPAddressField(default='0.0.0.0', unique=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='full_name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
