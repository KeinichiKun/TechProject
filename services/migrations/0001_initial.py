# Generated by Django 3.0.4 on 2020-03-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_caption', models.CharField(max_length=20, verbose_name='Наименование продукта')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('quantity_in_stock', models.IntegerField(verbose_name='Количество на складе')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
