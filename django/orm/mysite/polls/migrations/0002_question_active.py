# Generated by Django 5.1.2 on 2024-11-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
