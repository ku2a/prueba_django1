# Generated by Django 4.2.7 on 2024-11-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_task"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="done",
            field=models.BooleanField(default=False),
        ),
    ]
