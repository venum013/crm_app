# Generated by Django 5.0 on 2023-12-18 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0004_remove_science_teams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='team',
        ),
    ]
