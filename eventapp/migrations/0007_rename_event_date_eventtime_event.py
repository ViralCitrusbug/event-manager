# Generated by Django 4.0.3 on 2022-03-22 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0006_alter_eventtime_event_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventtime',
            old_name='event_date',
            new_name='event',
        ),
    ]
