from django.forms import ModelForm

from .models import *


class EntrepriseForm(ModelForm):
    class Meta:
        model = Entreprise
        fields = '__all__'


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ReclamationForm(ModelForm):
    class Meta:
        model = Reclamation
        fields = '__all__'