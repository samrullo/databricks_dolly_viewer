# Generated by Django 4.2 on 2023-04-16 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatabrickModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.TextField()),
                ('context', models.TextField()),
                ('response', models.TextField()),
                ('category', models.CharField(max_length=250)),
            ],
        ),
    ]