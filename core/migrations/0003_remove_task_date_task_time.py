# Generated by Django 5.1.7 on 2025-03-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_name_task_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.DateTimeField(default=None),
        ),
    ]
