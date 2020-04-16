from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView
from .models import Cars, Expenses, Profit, Repairs, Repairs_type, Worker


# Create your views here.

def cars(request):
    cars = Cars.objects.all()
    return render(request, 'cars.html', {'cars': cars})

def car(request):
    car = Cars.objects.get(id=id)
    return render(request, 'more_details_car.html', {'car': car})


# добавление данных в бд
def create(request):

    if request.method == "POST":
        tom = Cars()
        tom.state_number = request.POST.get("state_number")
        tom.Model_caption = request.POST.get("Model_caption")
        tom.Spec_caption = request.POST.get("Spec_caption")
        tom.Mark_caption = request.POST.get("Mark_caption")
        tom.carrying = request.POST.get("carrying")
        tom.rent = request.POST.get("rent")
        tom.save()
        return HttpResponseRedirect("/cars")
    else:
        return render(request, "create_car.html")

def create_profit(request , id):
    car = Cars.objects.get(id=id)
    if request.method == "POST":
        tom = Profit()
        tom.car = car.id
        tom.description = request.POST.get("description")
        tom.cost = request.POST.get("cost")
        tom.save()
        return HttpResponseRedirect("/cars/detail/")
    else:
        return render(request, "create_profit.html")

def create_expenses(request, id):
    car = Cars.objects.get(id=id)
    if request.method == "POST":
        tom = Expenses()
        tom.car = car
        tom.description = request.POST.get("description")
        tom.cost = request.POST.get("cost")
        tom.data = request.POST.get("data")
        tom.save()
        return HttpResponseRedirect("/cars/detail/" + str(car.id))
    else:
        return render(request, "create_expenses.html", {"car": car})

# изменение данных в бд
def edit(request, id):
    try:
        profit = Profit.objects.filter(car=id)
        expenses = Expenses.objects.filter(car=id)
        rep = Repairs.objects.filter(car=id)
        Profit.objects.order_by('data')
        Expenses.objects.order_by('data')
        car = Cars.objects.get(id=id)

        if request.method == "POST":
            car.state_number = request.POST.get("state_number")
            car.expenses = request.POST.get("expenses")
            car.Model_caption = request.POST.get("Model_caption")
            car.Spec_caption = request.POST.get("Spec_caption")
            car.Mark_caption = request.POST.get("Mark_caption")
            car.carrying = request.POST.get("carrying")
            car.rent = request.POST.get("rent")
            car.save()
            return HttpResponseRedirect("/cars")
        else:

                return render(request, "more_details_car.html", {"car": car, "profit": profit, "expenses": expenses, 'rep': rep})
    except Cars.DoesNotExist:
        return HttpResponseNotFound("<h2>Автомобиль не найден</h2>")

def editEx(request, id):
    try:

        tom = Expenses.objects.get(id=id)
        if request.method == "POST":
            tom.description = request.POST.get("description")
            tom.cost = request.POST.get("cost")
            tom.data = request.POST.get("data")
            tom.save()
            return HttpResponseRedirect("/cars/detail/" + str(car.id))
        else:
               return render(request, "edit_expenses.html",  {"expenses": tom})
    except Expenses.DoesNotExist:
        return HttpResponseNotFound("<h2>customer не найден</h2>")

# удаление данных из бд
def delete(request, id):
    try:
        cars = Cars.objects.get(id=id)
        cars.delete()
        return HttpResponseRedirect("/cars")
    except Cars.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def deleteEx(request, id):
    try:
        car = Cars.objects.get(id=id)
        expenses = Expenses.objects.get(id=id)
        expenses.delete()
        return HttpResponseRedirect("/cars/detail/" + str(car.id))
    except Cars.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")



def create_rep(request, id):
    type = Repairs_type.objects.all()
    worker = Worker.objects.all()
    car = Cars.objects.get(id=id)
    if request.method == "POST":
        tom = Repairs()
        type = Repairs_type()
        worker = Worker()
        tom.car = car
        tom.data_start = request.POST.get("data_start")
        tom.data_end = request.POST.get("data_end")
        tom.description = request.POST.get("description")
        tom.type = type
        tom.worker = worker
        tom.save()
        return HttpResponseRedirect("/cars/detail/" + str(car.id))
    else:
        return render(request, "create_rep.html", {"car": car, "type": type, "worker": worker})



class Serch(ListView):
    # поиск

    def get_queryset(self):
        return Cars.objects.filter(state_number__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get("q")
        return context
