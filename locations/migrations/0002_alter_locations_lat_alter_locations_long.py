# Generated by Django 4.1.3 on 2023-02-08 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='lat',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='locations',
            name='long',
            field=models.CharField(max_length=255),
        ),
    ]
