# Generated by Django 3.1.14 on 2023-02-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_alter_members_is_connected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
