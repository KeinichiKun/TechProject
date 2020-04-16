from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.base import View

from .models import Product

# Create your views here.
def services(request):
    product = Product.objects.all()
    return render(request, 'services.html', {'product': product})

# добавление данных в бд
def create(request):
    if request.method == "POST":
        tom = Product()
        tom.product_caption = request.POST.get("product_caption")
        tom.price = request.POST.get("price")
        tom.quantity_in_stock = request.POST.get("quantity_in_stock")
        tom.save()
        return HttpResponseRedirect("/services")
    else:
        return render(request, "create_product.html")

# изменение данных в бд
def edit(request, id):
    try:
        tom = Product.objects.get(id=id)
        if request.method == "POST":
            tom.product_caption = request.POST.get("product_caption")
            tom.price = request.POST.get("price")
            tom.quantity_in_stock = request.POST.get("quantity_in_stock")
            tom.save()
            return HttpResponseRedirect("/services")
        else:
               return render(request, "edit_product.html", {"product": tom})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Товар не найден</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/services")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")



class SerchProduct(ListView):


    template_name = 'services.html'

    def get_queryset(self):
        return Product.objects.filter(product_caption__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context



"""
class SerchProduct(ListView):
    model = Product
    template_name = 'services.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        product = Product.objects.filter(Q(product_caption__icontains=query))
        return product
    
"""

