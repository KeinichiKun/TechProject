# Generated by Django 3.0.4 on 2020-03-31 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20200331_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сustomer',
            name='T_customer',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.Type_customer', verbose_name='Тип заказчика'),
        ),
    ]