# Generated by Django 4.1.3 on 2023-04-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0006_alter_reservemodel_date_alter_reservemodel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservemodel',
            name='date',
            field=models.DateField(default='2023-01-01', verbose_name='روز'),
        ),
        migrations.AlterField(
            model_name='reservemodel',
            name='time',
            field=models.TimeField(default='08:00:00', verbose_name='زمان'),
        ),
    ]