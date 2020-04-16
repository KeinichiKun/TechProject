from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('search_product/', views.SerchProduct.as_view(), name='search_product'),
    path('edit/<int:id>/', views.edit),
    path('create/', views.create),
    path('delete/<int:id>/', views.delete),
]