# Generated by Django 3.0.4 on 2020-05-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200427_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='householder',
            name='pic',
            field=models.ImageField(upload_to='media'),
        ),
    ]