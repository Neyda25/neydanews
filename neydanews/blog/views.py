from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#MVT
#model, view template, 
#Importaciones de la libreria personal
from . import models 


def listar_noticias(request):
	"""
		Obtiene las noticias de la base de datos 

		Retorna:
			El listado de las noticias
	"""
	#obtiene el listado de todas las noticias 
	#De la base de datos y la asigna a la variable
	#noticias
	noticias = models.Noticia.objects.all()

	#Retorna todo renderizado para ser leido en el
	#explorador, tiene tres parametros
	#Solicitud(request), plantilla de datos y datos
	#los datos deben de ir en diccionario 
	return render(
					request, 
					'./noticias/index.html',
					 {"news":noticias}
				)

def ver_noticia(request, id_noticia):
	"""
	obtiene noticias de la base de datos

	parametros:
		id_noticia es numerico y hace referencia 
		al identificador de la noticia buscada

	Retorna:
		La noticia busca si existe
	"""

	noticia =  models.Noticia.objects.get(id=id_noticia)

	return render(
					request,
					'./noticias/detalles.html',
					{"noticia":noticia}

				)