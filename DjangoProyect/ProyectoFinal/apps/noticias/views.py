from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

# Create your views here.
from .models import Noticia, Categoria
from .forms import Form_Alta

#CONTROLA SI EL USUARIO ESTA LOGEADO
from django.contrib.auth.mixins import LoginRequiredMixin

class CrearNoticia(LoginRequiredMixin, CreateView):
	model = Noticia
	form_class = Form_Alta
	template_name = 'noticias/CrearNoticia.html'
	success_url = reverse_lazy('noticias:listar_noticias')

	def form_valid(self, form):
		noticia = form.save(commit=False)
		noticia.autor = self.request.user
		return super(CrearNoticia, self).form_valid(form)



class ListarNoticias(ListView):
	model = Noticia
	template_name = 'noticias/listar.html'
	#POR DEFECTO ESTA VISTA MANDA AL TEMPLATE UNA VARIABLE
	#LLAMADA OBJECT_LIST, CON LA LISTA DE TODAS LAS NOTICIAS



def ListarNoticiasF(request):
	ctx = {}

	todas_las_noticias = Noticia.objects.all()

	ctx['object_list'] = todas_las_noticias

	return render(request, 'noticias/listar.html', ctx)



def DetalleNoticiaF(request, pk):
	ctx = {}

	datos_noticia = Noticia.objects.get(id = pk)

	ctx['detalle'] = datos_noticia

	return render(request, 'noticias/detalle.html', ctx)


class Categorias(ListView):
	model = Categoria
	template_name = 'noticias/categorias.html'


def Filtro_Cat(request, pk):
	ctx = {}

	nombre_categoria = Categoria.objects.get(id = pk)

	noticias_filtradas = Noticia.objects.filter(categoria = nombre_categoria)

	ctx['object_list'] = noticias_filtradas

	return render(request, 'noticias/listar.html', ctx)
