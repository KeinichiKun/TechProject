# Generated by Django 3.0.4 on 2020-04-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20200331_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='сustomer',
            name='bank',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Банк'),
        ),
        migrations.AddField(
            model_name='сustomer',
            name='bik',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='БИК'),
        ),
        migrations.AddField(
            model_name='сustomer',
            name='email',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='сustomer',
            name='inn',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='ИНН'),
        ),
        migrations.AddField(
            model_name='сustomer',
            name='kpp',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='КПП'),
        ),
        migrations.AddField(
            model_name='сustomer',
            name='ks',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Корр. счет'),
        ),
        migrations.AddField(
            model_name='сustomer',
            name='rs',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='р/с'),
        ),
    ]