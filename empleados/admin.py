from django.contrib import admin       

from empleados.models import Empleado, Empresa, Cargo
                                    

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre', 'activa',)
	list_filter = ('nombre',)
	search_fields = ('codigo', 'nombre','correo',)


class CargoAdmin(admin.ModelAdmin):
	list_display = ('id', 'cargo',)
	list_filter = ('cargo',)
	search_fields = ('cargo',)


class EmpleadoAdmin(admin.ModelAdmin):
	list_display = ('identificacion', 'nombres', 'apellido_paterno',)
	list_filter = ('cargo',)
	search_fields = ('identificacion', 'nombres',)


admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Empresa,EmpresaAdmin)         
admin.site.register(Cargo,CargoAdmin)         