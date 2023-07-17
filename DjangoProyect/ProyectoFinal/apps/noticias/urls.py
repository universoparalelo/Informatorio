from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('CrearNoticia', views.CrearNoticia.as_view(), name = 'CrearNoticia'),

    path('Listar', views.ListarNoticias.as_view(), name="listar_noticias"),
]