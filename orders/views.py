from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Order, Cars, Worker, Сustomer, Product

# Create your views here.

def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})


# добавление данных в бд
def create(request):
    car = Cars.objects.all()
    customer = Сustomer.objects.all()
    worker = Worker.objects.all()
    product = Product.objects.all()
    if request.method == "POST":
        tom = Order()
        car = Cars()
        worker = Worker()
        customer = Сustomer()
        product = Product()
        car.id = request.POST.get("car")
        worker.id = request.POST.get("worker")
        customer.id = request.POST.get("customer")
        product.id = request.POST.get("product")

        tom.car = car
        tom.worker = worker
        tom.customer = customer
        tom.product = product
        tom.quantity = request.POST.get("quantity")
        tom.time = request.POST.get("time")
        tom.final_price = request.POST.get("final_price")
        tom.adress = request.POST.get("adress")
        tom.save()
        return HttpResponseRedirect("/orders")
    else:
        return render(request, "create_order.html", {"car": car, "worker": worker, "customer": customer, "product": product})

# изменение данных в бд
def edit(request, id):
    try:
        car = Cars.objects.all()
        customer = Сustomer.objects.all()
        worker = Worker.objects.all()
        product = Product.objects.all()
        if request.method == "POST":
            tom = Order(id=id)
            car = Cars(id=id)
            worker = Worker(id=id)
            customer = Сustomer(id=id)
            product = Product(id=id)

            tom.car = car
            tom.worker = worker
            tom.customer = customer
            tom.product = product
            tom.quantity = request.POST.get("quantity")
            tom.time = request.POST.get("time")
            tom.final_price = request.POST.get("final_price")
            tom.adress = request.POST.get("adress")
            tom.save()
            return HttpResponseRedirect("/customers")
        else:
               return render(request, "edit_order.html", {"car": car, "worker": worker, "customer": customer, "product": product})
    except Сustomer.DoesNotExist:
        return HttpResponseNotFound("<h2>customer не найден</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        cars = Order.objects.get(id=id)
        cars.delete()
        return HttpResponseRedirect("/orders")
    except Order.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def complite(request, id):
    try:
            tom = Order.objects.get(id=id)
            tom.status = "C"
            tom.save()
            return HttpResponseRedirect("/orders")
    except Сustomer.DoesNotExist:
        return HttpResponseNotFound("<h2>customer не найден</h2>")



def search(ListView):
    # поиск
    def get_queryset(self):
        return Order.objects.filter(first_name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get("q")
        return context