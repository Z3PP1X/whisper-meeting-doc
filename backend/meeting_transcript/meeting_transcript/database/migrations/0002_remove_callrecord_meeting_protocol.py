# Generated by Django 5.0.6 on 2024-06-25 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="callrecord", name="meeting_protocol",),
    ]