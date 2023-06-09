# Generated by Django 4.1.3 on 2023-04-27 15:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_remove_roomtype_hotel_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='hotel',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='booking.hotel'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='arrive_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 22, 4, 52, 676306)),
        ),
    ]
