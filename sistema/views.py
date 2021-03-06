from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse 
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def index(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/privado')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:   
	    formulario = AuthenticationForm() 
	return render_to_response('ingresar.html', {'formulario':formulario}, context_instance=RequestContext(request))

                     
@login_required(login_url='/')
def privado(request):
	usuario = request.user
	return render_to_response('privado.html', {'usuario':usuario}, context_instance=RequestContext(request))


@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


@login_required(login_url='/')
def about(request):
	return render_to_response('about.html')


def verinfo(request):
	pass