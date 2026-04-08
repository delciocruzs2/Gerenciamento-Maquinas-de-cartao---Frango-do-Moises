from django.contrib import admin
from django.utils.html import format_html
from maquinas.models import *

@admin.register(Maquinas_Model)
class Maquinas_Admin(admin.ModelAdmin):
    list_display = ('id_maquina', 'exibir_foto', 'nome_maquina', 'valor_limite')
    search_fields = ('nome_maquina',)
    list_filter = ('nome_maquina',)

    def exibir_foto(self, obj):
        if obj.imagem_maquina:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 5px; object-fit: cover;" />', obj.imagem_maquina.url)
        return "Sem imagem"