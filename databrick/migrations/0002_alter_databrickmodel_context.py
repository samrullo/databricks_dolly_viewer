# Generated by Django 4.2 on 2023-04-16 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databrick', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databrickmodel',
            name='context',
            field=models.TextField(blank=True),
        ),
    ]
