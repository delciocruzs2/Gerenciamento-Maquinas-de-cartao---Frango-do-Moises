from django.urls import path
from transacao.views import *

urlpatterns = [
    path('lancamento/', Vendas_View.as_view(), name='lancamento'),
    path('venda/editar/<int:pk>/', Venda_Update_View.as_view(), name='editar_venda'),
    path('venda/excluir/<int:pk>/', excluir_venda_view, name='excluir_venda'),
]
