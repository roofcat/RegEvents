from django.db import models


class Empresa(models.Model):
	codigo = models.CharField(primary_key=True, max_length=60)
	nombre = models.CharField(max_length=120)
	activa = models.BooleanField(default=True)
	direccion = models.CharField(max_length=250)
	correo = models.EmailField()
	telefono = models.CharField(max_length=120)
	celular = models.CharField(max_length=120)
	
	def __unicode__(self):
		return self.nombre
		
		
class Cargo(models.Model):
	cargo = models.CharField(max_length=120)
	
	def __unicode__(self):
		return self.cargo


class Empleado(models.Model):
	identificacion = models.CharField(primary_key=True, max_length=15)
	nombres = models.CharField(max_length=120)
	apellido_paterno = models.CharField(max_length=120)
	apellido_materno = models.CharField(max_length=120)
	fecha_nacimiento = models.DateField()
	empresa = models.ForeignKey(Empresa)
	cargo = models.ForeignKey(Cargo)
	activo = models.BooleanField(default=True)
	foto = models.ImageField(upload_to='fotoperfil', verbose_name='Foto de Perfil')