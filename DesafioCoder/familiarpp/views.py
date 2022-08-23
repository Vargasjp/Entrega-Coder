from django.shortcuts import render
from familiarpp.models import Familia
import datetime
from django.http import HttpResponse
from django.template import loader
from urllib import request
from django.http import HttpRequest

# Create your views here.

def familia(self):
    madre=Familia(Nombre="Eleonora",Apellido="Bauza",Dni="17045100",FechaDeNac="1967-01-24")
    madre.save()
    hijo=Familia(Nombre="Juan Pablo", Apellido="Vargas",Dni="37687400",FechaDeNac="1993-07-14")
    hijo.save()
    mascota=Familia(Nombre="Alfreda",Apellido="Vargas",Dni="47657876",FechaDeNac="2017-10-25")
    mascota.save()
    mascota2=Familia(Nombre="Cristina",Apellido="Bauza",Dni="53457873",FechaDeNac="2018-10-15")
    mascota2.save()
    diccionario={"madre":madre,"hijo":hijo,"mascota":mascota,"mascota2":mascota2}
    plantilla=loader.get_template("template1.html")
    ejecutar=plantilla.render(diccionario)
    return HttpResponse(ejecutar)