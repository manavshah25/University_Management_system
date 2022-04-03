# Generated by Django 4.0.2 on 2022-04-03 22:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='number',
        ),
        migrations.AddField(
            model_name='student',
            name='phoneNumber',
            field=models.CharField(default=9512256617, max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
            preserve_default=False,
        ),
    ]
