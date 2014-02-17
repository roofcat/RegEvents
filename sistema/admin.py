from django.contrib import admin


from sistema.models import Sistema
                             

class SistemaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'correo',)
                             

admin.site.register(Sistema, SistemaAdmin)