# Generated by Django 4.1.3 on 2023-04-27 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_reservation_arrive_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='arrive_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 22, 43, 19, 520141)),
        ),
    ]
