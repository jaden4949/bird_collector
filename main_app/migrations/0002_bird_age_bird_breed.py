# Generated by Django 5.0.3 on 2024-03-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bird',
            name='breed',
            field=models.CharField(default='', max_length=100),
        ),
    ]
