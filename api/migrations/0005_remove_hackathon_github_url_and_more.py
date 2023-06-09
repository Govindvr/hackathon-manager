# Generated by Django 4.2 on 2023-04-20 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_submission_hackathonparticipant"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hackathon",
            name="github_url",
        ),
        migrations.RemoveField(
            model_name="hackathon",
            name="other_url",
        ),
        migrations.RemoveField(
            model_name="submission",
            name="github_url",
        ),
        migrations.RemoveField(
            model_name="submission",
            name="other_url",
        ),
        migrations.AddField(
            model_name="hackathon",
            name="submission_type",
            field=models.CharField(
                choices=[("image", "Image"), ("file", "File"), ("link", "Link")],
                default="link",
                max_length=5,
            ),
        ),
        migrations.AddField(
            model_name="submission",
            name="submission",
            field=models.TextField(blank=True),
        ),
    ]
