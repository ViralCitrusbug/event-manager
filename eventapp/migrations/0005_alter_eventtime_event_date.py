# Generated by Django 4.0.3 on 2022-03-22 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0004_alter_eventtime_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtime',
            name='event_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.eventdate'),
        ),
    ]
