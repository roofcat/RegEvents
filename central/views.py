from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse 
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
             

from central.forms import EventoForms


def nuevoevento(request):
	if request == 'POST':
		evento_form = EventoForm(request.POST)
		if evento_form.is_valid():
			evento = evento_form.save(commit=False)
			evento.usuario = request.user
			evento.save()            
			return HttpResponseRedirect('/nuevoevento')
	else:
		evento_form = EventoForm()
	return render_to_response('nuevoevento.html',{'evento_form':evento_form},context_instance=RequestContext(request,locals()))


