from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()                                

from sistema.views import index
from central.views import nuevoevento 

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'sistema.views.index'), 
	url(r'^privado/$', 'sistema.views.privado'), 
	url(r'^cerrar/$', 'sistema.views.cerrar', name='logout'),
	url(r'^about/$', 'sistema.views.about', name='about'),
)
