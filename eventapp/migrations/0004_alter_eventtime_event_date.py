# Generated by Django 4.0.3 on 2022-03-22 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtime',
            name='event_date',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eventapp.event'),
        ),
    ]
