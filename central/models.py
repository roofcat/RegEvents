from django.db import models  
from django.contrib.auth.models import User


class Clave(models.Model): 
	codigo = models.CharField(primary_key=True, max_length=60)
	nombre = models.CharField(max_length=120)
	descripcion = models.CharField(max_length=250)

	def __unicode__(self):
		return self.nombre
                

class Sucursal(models.Model):
	codigo = models.CharField(primary_key=True, max_length=60)
	sucursal = models.CharField(max_length=120)
	activa = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.sucursal


class Evento(models.Model): 
	clave = models.ForeignKey(Clave)
	sucursal = models.ForeignKey(Sucursal)
	fecha_registro = models.DateTimeField(auto_now=True) 
	usuario = models.ForeignKey(User)
	observaciones = models.TextField(max_length=250)
	
	def __unicode__(self):
		return self.observaciones
	