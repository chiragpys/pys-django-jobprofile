# Generated by Django 4.2.4 on 2023-09-01 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidateprofile',
            old_name='date',
            new_name='created',
        ),
    ]
