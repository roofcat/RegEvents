from django.forms import ModelForm


from central.models import Evento, Sucursal, Clave
                 

class EventoForm(ModelForm):
	
	class Meta:
		model = Evento
		fields = ['clave', 'sucursal', 'observaciones']


