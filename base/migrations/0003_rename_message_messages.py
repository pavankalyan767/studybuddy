# Generated by Django 3.2.12 on 2024-02-24 14:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_auto_20240224_1409'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Messages',
        ),
    ]
