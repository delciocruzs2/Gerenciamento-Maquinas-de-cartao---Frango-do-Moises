from django import forms
from maquinas.models import *

class Maquina_Form(forms.ModelForm):
    class Meta:
        model = Maquinas_Model
        fields = ['nome_maquina','valor_limite','dia_vencimento','imagem_maquina']