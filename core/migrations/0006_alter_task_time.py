# Generated by Django 5.1.7 on 2025-03-19 22:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
