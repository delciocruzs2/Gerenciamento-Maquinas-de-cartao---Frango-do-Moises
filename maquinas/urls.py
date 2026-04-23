from django.urls import path
from maquinas.views import *
from transacao.views import Financeiro_Maquina_View

urlpatterns = [
    path('gerenciador_maquinas/', Maquina_View.as_view(), name='gerenciador_maquinas'),
    path('adicionar_maquinas/', Adicionar_Maquina_View.as_view(), name='adicionar_maquinas'),
    path('atualizar_maquina/<int:id>/', Atualizar_Maquina_View.as_view(), name='atualizar_maquina'),
    path('deletar_maquina/<int:id>/', Deletar_Maquina_View.as_view(), name='deletar_maquina'),
    path('financeiro/<int:maquina_id>/', Financeiro_Maquina_View.as_view(), name='financeiro_maquina'),
]

