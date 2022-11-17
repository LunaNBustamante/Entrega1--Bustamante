from django.shortcuts import render
from django.http import HttpResponse
from AppConciertos.models import Bandas
from django.template import loader
# Create your views here.

#Creamos la funcion de view

#Creamos la funcion de view

def nombre_banda(request):

    lista_banda = Bandas.objects.all()

    datos = {'lista_banda': lista_banda}
    

#Obtengo el template
    plantilla = loader.get_template('templates.html')


    #Renderizacion de datos

    doc = plantilla.render(datos)

    return HttpResponse(doc)