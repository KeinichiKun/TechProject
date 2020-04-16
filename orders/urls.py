from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('complite/<int:id>/', views.complite, name='complite'),
]