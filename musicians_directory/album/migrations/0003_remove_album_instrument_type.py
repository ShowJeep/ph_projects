# Generated by Django 5.0 on 2024-01-30 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_album_instrument_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='instrument_type',
        ),
    ]
