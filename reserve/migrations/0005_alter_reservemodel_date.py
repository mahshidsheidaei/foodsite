# Generated by Django 4.1.3 on 2023-04-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0004_alter_reservemodel_date_alter_reservemodel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservemodel',
            name='date',
            field=models.DateField(default='2023-5-4', verbose_name='روز'),
        ),
    ]