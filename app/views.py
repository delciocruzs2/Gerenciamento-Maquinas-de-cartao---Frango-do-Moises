from django.shortcuts import render, redirect
from django.views import View
from maquinas.models import *
from transacao.models import *
from django.db.models import Sum
from datetime import date
    
# Sessao: Logica da Home
from django.views import View
from django.shortcuts import render
from django.db.models import Sum
from maquinas.models import Maquinas_Model
from transacao.models import Vendas_Model

from django.views import View
from django.shortcuts import render
from django.db.models import Sum
from maquinas.models import Maquinas_Model
from transacao.models import Vendas_Model

from django.views import View
from django.shortcuts import render
from django.db.models import Sum
from maquinas.models import Maquinas_Model
from transacao.models import Vendas_Model

from django.views import View
from django.shortcuts import render
from django.db.models import Sum
from maquinas.models import Maquinas_Model
from transacao.models import Vendas_Model

from django.views import View
from django.shortcuts import render
from django.db.models import Sum
from maquinas.models import Maquinas_Model
from transacao.models import Vendas_Model

from django.views import View
from django.shortcuts import render
from django.db.models import Sum
from maquinas.models import Maquinas_Model
from transacao.models import Vendas_Model

class Home_View(View):
    def get(self, request):
        maquinas = Maquinas_Model.objects.all()
        
        for m in maquinas:
            total = Vendas_Model.objects.filter(maquina_to_venda=m).aggregate(Sum('valor_venda'))['valor_venda__sum'] or 0
            
            m.total_gasto = total
            m.valor_disponivel = m.valor_limite - total
            
            if m.valor_limite > 0:
                m.porcentagem = (total / m.valor_limite) * 100
            else:
                m.porcentagem = 0
            
            if m.porcentagem >= 100:
                m.cor_barra = "#FF0000"
                m.porcentagem_barra = 100
            elif m.porcentagem >= 80:
                m.cor_barra = "#CC4400"
                m.porcentagem_barra = m.porcentagem
            elif m.porcentagem > 50:
                m.cor_barra = "#FFFF66"
                m.porcentagem_barra = m.porcentagem
            else:
                m.cor_barra = "#28a745"
                m.porcentagem_barra = m.porcentagem

        return render(request, 'home.html', {'maquinas': maquinas})