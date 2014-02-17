from django.contrib import admin


from central.models import Clave, Sucursal, Evento
     

class ClaveAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre', 'descripcion',)
	list_filter = ('nombre',)
	search_fields = ('codigo', 'nombre',)


class SucursalAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'sucursal', 'activa',)
	list_filter = ('sucursal',)
	search_fields = ('codigo', 'sucursal',)


class EventoAdmin(admin.ModelAdmin):
	list_display = ('clave','sucursal','fecha_registro','usuario',)
	list_filter = ('fecha_registro',)
	search_fields = ('clave', 'sucursal',)
                            
admin.site.register(Clave, ClaveAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Evento, EventoAdmin)