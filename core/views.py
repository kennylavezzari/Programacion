from django.shortcuts import render,HttpResponse,redirect,reverse
from .models import acercade,contacto,portada,menu,portafolios,datospersonales
from .forms import Contactform
from django.core.mail import EmailMessage

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

def contacto(request):
    contact_form = Contactform()
    if request.method == 'POST':
        contact_form = Contactform(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #creamos el correo de
            email = EmailMessage(
                "Mundo de Programacion: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["kolavezzari@est.itsgg.edu.ec"],
                reply_to=[email]
            )
            #lo enviamos y redireccionamos
            try:
                email.send()
                return redirect(reverse('contacto') + "?okey")
            except:
                return redirect(reverse('contacto') + "?fail")

            return redirect(redirect('contacto') + "?okey")

    return render(request,'contacto.html',{'formulario':contact_form})

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


def buscardatospersonales(request):
    return render(request, 'buscardatospersonales.html',)

def buscarpdatospersonalesview(request):
    if request.GET["pwd"]:
        mensaje="los datos  buscados son :%r" %request.GET["pwd"]
        pwd=request.GET["pwd"]
        objetos = datospersonales.objects.filter(cedula=pwd)
        return render(request, 'datospersonales.html', {'valores': objetos})
    else:
        mensaje = "por favor ingrese la cedula a buscar"
    return HttpResponse(mensaje)


def buscaracercade(request):
    return render(request, 'buscaracercade.html',)

def buscaracercadeview(request):
    if request.GET["pwd"]:
        mensaje="los titulos  buscados son :%r" %request.GET["pwd"]
        pwd=request.GET["pwd"]
        objetos = acercade.objects.filter(titulo=pwd)
        return render(request, 'acercade.html', {'valores': objetos})
    else:
        mensaje = "por favor ingrese el titulo a buscar"
    return HttpResponse(mensaje)


def buscarcontacto(request):
    return render(request, 'buscarcontacto.html',)

def buscarcontactoview(request):
    if request.GET["pwd"]:
        mensaje="los titulos  buscados son :%r" %request.GET["pwd"]
        pwd=request.GET["pwd"]
        objetos = contacto.objects.filter(titulo=pwd)
        return render(request, 'contacto.html', {'valores': objetos})
    else:
        mensaje = "por favor ingrese el titulo a buscar"
    return HttpResponse(mensaje)


def buscarindex(request):
    return render(request, 'buscarindex.html',)

def buscarindexview(request):
    if request.GET["pwd"]:
        mensaje="los titulos  buscados son :%r" %request.GET["pwd"]
        pwd=request.GET["pwd"]
        objetos = portada.objects.filter(titulo=pwd)
        return render(request, 'index.html', {'valores': objetos})
    else:
        mensaje = "por favor ingrese el titulo a buscar"
    return HttpResponse(mensaje)


def buscarmenu(request):
    return render(request, 'buscarnenu.html',)

def buscarmenuview(request):
    if request.GET["pwd"]:
        mensaje="los titulos  buscados son :%r" %request.GET["pwd"]
        pwd=request.GET["pwd"]
        objetos = menu.objects.filter(titulo=pwd)
        return render(request,'menu.html',{'valores':objetos})
    else:
        mensaje = "por favor ingrese el titulo a buscar"
    return HttpResponse(mensaje)



