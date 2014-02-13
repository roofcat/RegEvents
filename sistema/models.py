from django.db import models


class Sistema(models.Model):
	nombre = models.CharField(max_length=120)
	correo = models.EmailField(max_length=120)
	anexo1 = models.CharField(max_length=20)
	anexo2 = models.CharField(max_length=20)
	telefono = models.CharField(max_length=20)
	celular = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.nombre