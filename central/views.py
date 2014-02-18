from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse 
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView
             
from django.utils import timezone
from central.models import Evento
from central.forms import EventoForm


@login_required
def nuevoevento(request):
	if request == 'POST':
		formulario = EventoForm(request.POST)
		if formulario.is_valid():
			evento = formulario.save(commit=False)
			evento.usuario = request.usuario
			evento.save()
			return HttpResponseRedirect('/nuevoevento')
	else:
		formulario = EventoForm()
	return render_to_response('nuevoevento.html',{'formulario':formulario},context_instance=RequestContext(request, locals()))


