# Generated by Django 4.2 on 2023-04-28 20:17

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Sub Title', models.CharField(max_length=50)),
                ('Description', models.TextField(verbose_name=builtins.max)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.TextField(verbose_name=builtins.max)),
            ],
        ),
    ]