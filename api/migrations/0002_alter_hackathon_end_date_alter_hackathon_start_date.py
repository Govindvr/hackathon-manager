# Generated by Django 4.2 on 2023-04-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hackathon",
            name="end_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="hackathon",
            name="start_date",
            field=models.DateField(),
        ),
    ]
