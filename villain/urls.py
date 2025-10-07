
from django.urls import path
from . import views


urlpatterns = [
    path('lista-viloes/', views.lista_viloes, name='lista_viloes'),
    path('hello-viloes/', views.hello_villains, name='hello_villains'),
    path('novo-vilao/', views.criar_vilao, name='criar_vilao'),
]