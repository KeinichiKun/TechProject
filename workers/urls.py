from django.urls import path
from . import views

urlpatterns = [
    path('', views.workers, name='workers'),
    path('search_workers/', views.Serch.as_view, name='search_workers'),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('tabel/<int:id>/', views.tabel),
]