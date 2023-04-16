# Generated by Django 4.1.3 on 2023-04-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReserveModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=300, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=20, verbose_name='شماره تلفن')),
                ('number', models.IntegerField(verbose_name='تعدادنفرات')),
                ('date', models.DateField(verbose_name='روز')),
                ('time', models.TimeField(verbose_name='زمان')),
            ],
        ),
    ]
