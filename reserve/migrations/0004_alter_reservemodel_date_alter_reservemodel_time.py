# Generated by Django 4.1.3 on 2023-04-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0003_alter_reservemodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservemodel',
            name='date',
            field=models.DateField(default='2023/5/4', verbose_name='روز'),
        ),
        migrations.AlterField(
            model_name='reservemodel',
            name='time',
            field=models.TimeField(default='13:20:00', verbose_name='زمان'),
        ),
    ]