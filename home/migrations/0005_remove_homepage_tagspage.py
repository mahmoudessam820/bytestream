# Generated by Django 5.1.6 on 2025-03-18 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_tagspage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='tagspage',
        ),
    ]
