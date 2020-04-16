from django.db import models
from cars.models import Cars
from workers.models import Worker
from customers.models import Сustomer
from services.models import Product


# Create your models here.
class Order(models.Model):
    car = models.ForeignKey(Cars, verbose_name="Автомобиль", on_delete=models.SET_NULL, null=True)
    worker = models.ForeignKey(Worker, verbose_name="Работник", on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Сustomer, verbose_name="Заказчик", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(verbose_name="Количество", null=True, blank=True)
    time = models.IntegerField(verbose_name="Время", null=True, blank=True)
    final_price = models.IntegerField(verbose_name="Итоговая стоимость")
    adress = models.CharField(max_length=20, verbose_name="Адрес")
    STATUS = (
        ('С', 'Сompleted'),
        ('D', 'During'),
    )
    status = models.CharField(max_length=1, choices=STATUS, verbose_name="Статус", default='D', null=True)

    def __str__(self):
        return str(self.id) + " " + self.adress

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural ="Заказы"