from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse 
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
             

from .models import Clave, Sucursal
from .forms import EventoForm

  
@login_required(login_url='/')
def nuevoevento(request):
	if request == 'POST':
		evento_form = EventoForm(request.POST)
		if evento_form.is_valid():
			form = evento_form.save(commit=False)
			form.usuario = request.user
			form.save()            
			return HttpResponseRedirect('/nuevoevento')
	else:
		evento_form = EventoForm()
		usuario = request.user
	return render_to_response('nuevoevento.html',{'evento_form':evento_form},context_instance=RequestContext(request,locals()))


class ClavesListView(ListView):
	template_name = 'listarclaves.html'
	model = Clave


class SucursalesListView(ListView):
	template_name = 'listarsucursales.html'
	model = Sucursal
	