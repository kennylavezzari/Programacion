from django.db import models
# Create your models here.


class categoria (models.Model):
    nombrecategoria=models.CharField(max_length=100)
    fecharegistro=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombrecategoria


class acercade(models.Model):
    titulo=models.CharField(max_length=200)
    content=models.TextField()
    imagen=models.ImageField(upload_to="imagenes")
    fecharegistro=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo


class inicio(models.Model):
    titulo = models.CharField(max_length=50)
    contentenido = models.TextField()
    imagen = models.ImageField(upload_to="imagenes")
    fecharegistro=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo

class contacto(models.Model):
    titulo = models.CharField(max_length=50)
    contentenido = models.TextField()
    imagen = models.ImageField(upload_to="imagenes")
    def __str__(self):
        return self.titulo

class portada(models.Model):
    titulo = models.CharField(max_length=50)
    contentenido = models.TextField()
    imagen = models.ImageField(upload_to="imagenes")
    def __str__(self):
        return self.titulo


class menu(models.Model):
    titulo = models.CharField(max_length=50)
    contentenido = models.TextField()
    imagen = models.ImageField(upload_to="imagenes")
    def __str__(self):
        return self.titulo


class portafolios(models.Model):
    titulo = models.CharField(max_length=50)
    contentenido = models.TextField()
    imagen = models.ImageField(upload_to="imagenes")
    def __str__(self):
        return self.titulo

class datospersonales(models.Model):
    cedula= models.CharField(max_length=10)
    apellido= models.CharField(max_length=50)
    direccion= models.CharField(max_length=100)
    def __str__(self):
        return self.apellido
# Create your models here.




