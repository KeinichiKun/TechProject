# Generated by Django 3.0.4 on 2020-04-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_profit_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
