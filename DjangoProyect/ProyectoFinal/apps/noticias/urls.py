from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('CrearNoticia', views.CrearNoticia.as_view(), name = 'CrearNoticia'),

    # path('Listar', views.ListarNoticias.as_view(), name="listar_noticias"),

    path('Listar', views.ListarNoticiasF, name="listar_noticias"),

    path('Detalle/<int:pk>', views.DetalleNoticiaF, name="detalle_noticia"),

    path('Categorias', views.Categorias.as_view(), name='categorias'),

    path('Filtro_Cat/<int:pk>', views.Filtro_Cat, name='filtro_cat'),

]