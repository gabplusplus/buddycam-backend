# Generated by Django 4.1.3 on 2023-02-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='streams',
            name='switch',
            field=models.BooleanField(default=False),
        ),
    ]