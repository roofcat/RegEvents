from django.conf.urls import patterns, include, url                                

from django.contrib import admin                

admin.autodiscover()                                

from sistema.views import index, cerrar, privado, about, verinfo
from central.views import nuevoevento, ClavesListView, SucursalesListView 

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),

	#app sistema
	url(r'^$', 'sistema.views.index'), 
	url(r'^privado/$', 'sistema.views.privado'), 
	url(r'^cerrar/$', 'sistema.views.cerrar', name='logout'),
	url(r'^about/$', 'sistema.views.about', name='about'),
	url(r'^verinfo/$', 'sistema.views.verinfo', name='verinfo'),
	 
	#app central
	url(r'^nuevoevento/$', 'central.views.nuevoevento', name='nuevoevento'),
	url(r'^listaclaves/$', ClavesListView.as_view(), name='listaclaves'),
	url(r'^listasucursales/$', SucursalesListView.as_view(), name='listasucursales'),
	
	#app empleados
	
)
