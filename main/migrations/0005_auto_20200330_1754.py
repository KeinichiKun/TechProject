# Generated by Django 3.0.4 on 2020-03-30 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200328_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='сustomer',
            name='T_customer',
        ),
        migrations.DeleteModel(
            name='Type_customer',
        ),
    ]
