# Generated by Django 4.1.3 on 2023-05-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0026_alter_roomtype_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='meal_type',
            field=models.TextField(choices=[('na', 'no meal'), ('t1', 'breakfast'), ('t2', 'dinner'), ('t3', 'breakfast and dinner')], default='na', max_length=11),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room_type',
            field=models.TextField(choices=[('single bedroom', 'Room Type 1'), ('double bedroom', 'Room Type 2'), ('queen size', 'Room Type 3'), ('king size', 'Room Type 4'), ('suite', 'Room Type 5'), ('apartment', 'Room Type 6')], default='single bedroom', max_length=14),
        ),
    ]
