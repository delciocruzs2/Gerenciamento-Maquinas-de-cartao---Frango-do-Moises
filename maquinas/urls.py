from django.urls import path
from maquinas.views import *

urlpatterns = [
    path('gerenciador_maquinas/', Maquina_View.as_view(), name='gerenciador_maquinas'),
    path('adicionar_maquinas/', Adicionar_Maquina_View.as_view(), name='adicionar_maquinas'),
]

