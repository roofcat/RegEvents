from django.contrib import admin       

from empleados.models import Empleado, Empresa, Cargo


admin.site.register(Empleado)         
admin.site.register(Empresa)         
admin.site.register(Cargo)         