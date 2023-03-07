from django.contrib import admin
from django.urls import path
from .views import main_menu

urlpatterns = [
    path('', main_menu),
    path('<str:menuName>/<int:id>', main_menu, name='currentFolder'),
]