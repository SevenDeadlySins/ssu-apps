from django.core import serializers

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from .models import Position

@dajaxice_register
def setSequences(request, value):
	dajax = Dajax()

	try:
		sequences = Position.objects.get(pk=value).sequence_set.all().order_by('sequence_num')
		json = serializers.serialize("json", sequences)
		dajax.add_data(json, 'setSequences')
	except ValueError:
		dajax.add_data(None, 'setSequences')

	return dajax.json()


@dajaxice_register
def noargsTest(request):
	dajax = Dajax()

	dajax.alert("No arguments!")
	
	return dajax.json()
