# Generated by Django 5.0 on 2023-12-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="content",
            field=models.TextField(default="Empty content here"),
        ),
    ]
