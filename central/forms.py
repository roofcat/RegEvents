from django import forms
from django.forms import ModelForm


from central.models import Evento
                 

class EventoForm(ModelForm):
	
	class Meta:
		model = Evento
		exclude = ['usuario',]


