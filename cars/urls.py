from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),

    path('search_car/', views.Serch.as_view(), name='search_car'),

    path('detail/<int:id>/', views.edit, name='detail_car'),
    path('create/', views.create),
    path('delete/<int:id>/', views.delete),


    path('detail/<int:id>/createpr/', views.create_profit),

    path('deleteEx/<int:id>/', views.deleteEx),
    path('detail/<int:id>/createex/', views.create_expenses),
    path('detail/editpr/<int:id>', views.editEx),

    path('detail/<int:id>/createrep/', views.create_rep),



]