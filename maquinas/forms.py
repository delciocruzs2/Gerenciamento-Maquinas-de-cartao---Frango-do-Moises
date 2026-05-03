from django import forms
from maquinas.models import Maquinas_Model

class Maquina_Form(forms.ModelForm):
    class Meta:
        model = Maquinas_Model
        fields = ['nome_maquina', 'valor_limite_anual', 'dia_vencimento', 'imagem_maquina']