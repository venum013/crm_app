# Generated by Django 5.0 on 2023-12-18 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0003_remove_teacher_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='science',
            name='teams',
        ),
    ]
