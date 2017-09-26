from django.db import models
from ckeditor.fields import RichTextField



# Tabla Info_pagina.
class Info_pagina(models.Model):
	twitter = models.CharField(max_length=15)
	facebook = models.CharField(max_length=30)
	telefono = models.CharField(max_length=8)
	email = models.EmailField(max_length=35)
	home_desc = models.TextField()
	habilidades_desc = models.TextField()
	trabajos_desc = models.TextField()

	def __str__(self):
		return "Informacion de la pagina"

	class Meta:
		verbose_name_plural = "Info de la Pagina"

#Tabla de Imagenes
class Imagenes(models.Model):
    imagen = models.ImageField(upload_to="images")
    descripcion = models.CharField(max_length=10)

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name_plural = 'Imagenes'

#Tipos de trabajos
TIPOS = (
    ("app", "APP"),
    ("web", "WEB"),)

# Tabla Trabajos
class Trabajos(models.Model):
    funciones = RichTextField(default='<ul><li></li></ul>')
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    abreviacion = models.CharField(max_length=10,default='null')
    tipo = models.CharField(max_length=3,choices=TIPOS)
    video = models.CharField(max_length=15,default='null')
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Trabajos'
#Tipos de habilidades
TIPOS_H = (
    ("lan", "Programming Language"),
    ("app", "Aplicacion"),
    ("web", "Web"),)
#Tabla Habilidades
class Habilidades(models.Model):
	nombre = models.CharField(max_length=20)
	tipo = models.CharField(max_length=3,choices=TIPOS_H, default='null')
	
	def __str__(self):
		return self.nombre
	class Meta:
		verbose_name_plural = 'Habilidades'