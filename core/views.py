from django.shortcuts import render,HttpResponse
from .models import acercade,contacto,portada,menu,portafolios,datospersonales
# Create your views here.
def holamundo(request):
    return render(request,'holamundo.html')

def portadaview(request):
    objetos = portada.objects.all()
    return render(request,'index.html',{'valores':objetos})

def menuview(request):
    objetos = menu.objects.all()
    return render(request,'menu.html',{'valores':objetos})

def portafolioview(request):
    objetos = portafolios.objects.all()
    return render(request,'portafolio.html',{'valores':objetos})

def contactoviews(request):
    objetos = contacto.objects.all()
    return render(request,'contacto.html',{'valores':objetos})

def acercadeview(request):
    objetos=acercade.objects.all()
    return render(request,'acercade.html',{'valores':objetos})


def datospersonalesview(request):
    objetos = datospersonales.objects.all()
    return render(request, 'datospersonales.html', {'valores': objetos})

def buscarportafolio(request):
    return render(request, 'buscarportafolio.html',)


def buscarportaview(request):
    if request.GET["pwd"]:
        mensaje="el portafolio buscado es :%r" %request.GET["pwd"]
        pwd=request.GET["pwd"]
        objetos = portafolios.objects.filter(titulo=pwd)
        return render(request, 'portafolio.html', {'valores': objetos})
    else:
        mensaje = "por favor ingrese el titulo a buscar"
    return HttpResponse(mensaje)



