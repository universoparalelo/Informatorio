
from django.urls import path, include
from . import views

app_name = 'productos'

urlpatterns = [
    path('catalogo', views.Catalogo, name = 'catalogo'),
]
