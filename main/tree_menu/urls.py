from django.contrib import admin
from django.urls import path
from .views import main_menu, home

urlpatterns = [
    path('', home),
    path('<str:menuName>/<int:id>', main_menu, name='currentFolder'),
]