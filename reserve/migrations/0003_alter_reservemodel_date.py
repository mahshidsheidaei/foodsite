# Generated by Django 4.1.3 on 2023-04-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0002_alter_reservemodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservemodel',
            name='date',
            field=models.DateField(verbose_name='روز'),
        ),
    ]
