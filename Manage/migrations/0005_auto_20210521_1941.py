# Generated by Django 3.1.6 on 2021-05-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manage', '0004_auto_20210521_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='mimg',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='mprice',
            field=models.IntegerField(default=0),
        ),
    ]