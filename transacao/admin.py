from django.contrib import admin
from transacao.models import *

@admin.register(Vendas_Model)
class Vendas_Admin(admin.ModelAdmin):
    list_display = ('valor_venda','data_venda','comprovante','maquina_to_venda')
    search_fields = ('valor_venda','data_venda','comprovante','maquina_to_venda')
    list_filter = ('valor_venda','data_venda','comprovante','maquina_to_venda')