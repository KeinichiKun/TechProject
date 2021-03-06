# Generated by Django 3.0.4 on 2020-03-19 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption_mark', models.CharField(max_length=20, verbose_name='Наименование марки')),
            ],
            options={
                'verbose_name': 'Марка',
                'verbose_name_plural': 'Марки',
            },
        ),
        migrations.CreateModel(
            name='Car_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption_model', models.CharField(max_length=20, verbose_name='Наименование модели')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.CreateModel(
            name='Car_specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption_spec', models.CharField(max_length=20, verbose_name='Наименование спецификации')),
            ],
            options={
                'verbose_name': 'Спецификация',
                'verbose_name_plural': 'Спецификации',
            },
        ),
        migrations.CreateModel(
            name='Type_car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrying', models.PositiveIntegerField(verbose_name='Грузоподъемность')),
                ('rent', models.PositiveIntegerField(verbose_name='Аренда')),
                ('Mark_caption', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.Car_mark', verbose_name='Марка')),
                ('Model_caption', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.Car_model', verbose_name='Модель')),
                ('Spec_caption', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.Car_specification', verbose_name='Спецификация')),
            ],
            options={
                'verbose_name': 'Тип автомобиля',
                'verbose_name_plural': 'Типы автомобилей',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_number', models.CharField(max_length=10, verbose_name='Гос номер')),
                ('expenses', models.PositiveIntegerField(verbose_name='Затраты')),
                ('income', models.PositiveIntegerField(verbose_name='Доход')),
                ('profit', models.IntegerField(verbose_name='Прибыль')),
                ('T_car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.Type_car', verbose_name='Тип автомобиля')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
