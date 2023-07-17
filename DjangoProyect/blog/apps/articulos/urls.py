from django.urls import path
from . import views

app_name = 'articulos'

urlpatterns = [
    path('articulo', views.Articulo, name='articulo')
]