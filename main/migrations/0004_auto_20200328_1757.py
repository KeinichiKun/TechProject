# Generated by Django 3.0.4 on 2020-03-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200328_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сustomer',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='сustomer',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='сustomer',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='сustomer',
            name='organization',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Организация'),
        ),
    ]
