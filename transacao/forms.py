from django import forms
from transacao.models import *

class Vendas_Form(forms.ModelForm):
    class Meta:
        model = Vendas_Model
        fields = ['valor_venda','data_venda','comprovante','maquina_to_venda']