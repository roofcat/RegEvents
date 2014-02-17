from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse 
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

from central.models import Evento

   
@login_required(login_url='/')
class nuevoevento(CreateView):
	model = Evento
	template_name = 'nuevoevento.html'
	success_url = '/'