# Generated by Django 5.0 on 2024-01-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='instrument_type',
            field=models.CharField(default=None, max_length=50),
        ),
    ]