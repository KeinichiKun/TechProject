# Generated by Django 3.0.4 on 2020-04-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_auto_20200408_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='сustomer',
            name='adres',
            field=models.CharField(blank=True, default='-', max_length=200, null=True, verbose_name='Адрес'),
        ),
    ]
