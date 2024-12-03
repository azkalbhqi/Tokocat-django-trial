import django.shortcuts
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('paint/', views.paint_list, name='paint_list'),
    path('create/', views.create_paint, name='create_paint'),
    path('update/<int:pk>/', views.update_paint, name='update_paint'),
    path('delete/<int:pk>/', views.delete_paint, name='delete_paint'),
]