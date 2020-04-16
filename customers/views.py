from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView, DeleteView
from django.views.generic.base import View

from .models import Сustomer, Type_customer



# Create your views here.

def customers(request):
    customer = Сustomer.objects.all()
    return render(request, 'customers.html', {'customer': customer})

# добавление данных в бд

def create(request):
    type = Type_customer.objects.all()
    if request.method == "POST":
        tom = Сustomer()
        type = Type_customer()
        type.id = request.POST.get("T_customer")
        tom.first_name = request.POST.get("last_name")
        tom.middle_name = request.POST.get("middle_name")
        tom.last_name = request.POST.get("last_name")
        tom.organization = request.POST.get("organization")
        tom.adres = request.POST.get("adres")
        tom.phone = request.POST.get("phone")
        tom.T_customer = type
        type.inn = request.POST.get("inn")
        tom.kpp = request.POST.get("kpp")
        tom.bank = request.POST.get("bank")
        tom.rs = request.POST.get("rs")
        tom.ks = request.POST.get("ks")
        tom.bik = request.POST.get("bik")
        tom.email = request.POST.get("email")
        tom.save()
        return HttpResponseRedirect("/customers")
    else:
        return render(request, "create_customer.html", {'type': type})

# изменение данных в бд
def edit(request, id):
    try:
        type = Type_customer.objects.all()
        customer = Сustomer.objects.get(id=id)
        if request.method == "POST":
            type = Type_customer(id=id)
            type.id = request.POST.get("T_customer")
            customer.first_name = request.POST.get("last_name")
            customer.middle_name = request.POST.get("middle_name")
            customer.last_name = request.POST.get("last_name")
            customer.organization = request.POST.get("organization")
            customer.adres = request.POST.get("adres")
            customer.phone = request.POST.get("phone")
            customer.T_customer = type
            customer.inn = request.POST.get("inn")
            customer.kpp = request.POST.get("kpp")
            customer.bank = request.POST.get("bank")
            customer.rs = request.POST.get("rs")
            customer.ks = request.POST.get("ks")
            customer.bik = request.POST.get("bik")
            customer.email = request.POST.get("email")
            customer.save()
            return HttpResponseRedirect("/customers")
        else:
               return render(request, "edit_customer.html", {"customer": customer, 'type': type})
    except Сustomer.DoesNotExist:
        return HttpResponseNotFound("<h2>customer не найден</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        customer = Сustomer.objects.get(id=id)
        customer.delete()
        return HttpResponseRedirect("/customers")
    except Сustomer.DoesNotExist:
        return HttpResponseNotFound("<h2>customers not found</h2>")



