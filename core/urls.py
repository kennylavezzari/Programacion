from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('hola', views.holamundo, name='core'),
    path('inicio', views.portadaview, name='inicio1'),
    path('menu', views.menuview, name='menu'),
    path('acercade', views.acercadeview, name='acerca'),
    path('', views.portafolioview, name='portafolio'),
    path('contacto', views.contactoviews, name='comtacto'),
    path('kenny_Lavezzari', views.datospersonalesview, name='datos'),
    path('buscarportafolio', views.buscarportafolio, name='buscaporta'),
    path('buscar/', views.buscarportaview),
    path('buscarpersonas', views.buscardatospersonales, name='buscaperonas'),
    path('buscarp/', views.buscarpdatospersonalesview),
    path('buscaracercade', views.buscaracercade, name='buscaacercade'),
    path('buscarac/', views.buscaracercadeview),
    path('buscarcontacto', views.buscarcontacto, name='buscarcontacto'),
    path('buscarcon/', views.buscarcontactoview),
    path('buscarindex', views.buscarindex, name='buscaindex'),
    path('buscarin/', views.buscarindexview),
    path('buscarmenu/', views.buscarmenu, name='buscamenu'),
    path('buscarme/', views.buscarmenuview)
]