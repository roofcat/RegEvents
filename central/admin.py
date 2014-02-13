from django.contrib import admin


from central.models import Clave, Sucursal, Evento

                            
admin.site.register(Clave)
admin.site.register(Sucursal)
admin.site.register(Evento)