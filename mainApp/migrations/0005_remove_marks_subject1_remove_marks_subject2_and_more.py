# Generated by Django 5.0.3 on 2024-03-28 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_alter_announcements_options_alter_announcements_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='subject1',
        ),
        migrations.RemoveField(
            model_name='marks',
            name='subject2',
        ),
        migrations.RemoveField(
            model_name='marks',
            name='subject3',
        ),
    ]
