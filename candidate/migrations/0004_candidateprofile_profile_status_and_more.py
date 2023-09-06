# Generated by Django 4.2.4 on 2023-09-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0003_rename_candidate_name_experiencedetail_candidate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofile',
            name='profile_status',
            field=models.CharField(choices=[('new', 'New'), ('active', 'Active'), ('rejected', 'Rejected'), ('assigned', 'Assigned'), ('closed', 'Closed')], default='new', max_length=50, verbose_name='Profile Status'),
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='reference',
            field=models.CharField(choices=[('agent', 'Agent'), ('other', 'Other')], default='other', max_length=50, verbose_name='Your Reference'),
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='reference_details',
            field=models.CharField(default='None', max_length=50, verbose_name='Reference Provider'),
        ),
    ]