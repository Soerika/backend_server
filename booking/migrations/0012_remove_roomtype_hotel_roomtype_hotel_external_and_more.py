# Generated by Django 4.1.3 on 2023-04-27 15:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_reservation_arrive_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomtype',
            name='hotel',
        ),
        migrations.AddField(
            model_name='roomtype',
            name='hotel_external',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='booking.hotel'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='arrive_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 22, 45, 2, 559455)),
        ),
    ]
