from django import forms
from maquinas.models import *

class Maquinha_Form(forms.ModelForm):
    class Meta:
        model = Maquinas_Model
        fields = ['nome_maquina','valor_limite']