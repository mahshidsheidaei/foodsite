# Generated by Django 4.1.3 on 2023-04-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservemodel',
            name='date',
            field=models.DateField(default='2023/10/2', verbose_name='روز'),
        ),
    ]