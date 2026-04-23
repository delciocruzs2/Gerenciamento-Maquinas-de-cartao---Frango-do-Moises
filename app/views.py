from django.views import View
from django.shortcuts import render
from django.db.models import Sum
from datetime import date, timedelta
from maquinas.models import Maquinas_Model
from transacao.models import Vendas_Model

class Home_View(View):
    def get(self, request):
        maquinas = Maquinas_Model.objects.all()
        hoje = date.today()
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
                 "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        
        for m in maquinas:
            if hoje.day < m.dia_vencimento:
                mes_inicio = hoje.month - 1 if hoje.month > 1 else 12
                ano_inicio = hoje.year if hoje.month > 1 else hoje.year - 1
                data_inicio = date(ano_inicio, mes_inicio, m.dia_vencimento)
                
                # O vencimento é no mês atual
                m.vencimento_completo = f"{m.dia_vencimento} de {meses[hoje.month - 1]}"
            else:
                data_inicio = date(hoje.year, hoje.month, m.dia_vencimento)
                
                # O vencimento já passou, então o próximo é no mês que vem
                prox_mes_idx = hoje.month if hoje.month < 12 else 0
                m.vencimento_completo = f"{m.dia_vencimento} de {meses[prox_mes_idx]}"

            total = Vendas_Model.objects.filter(
                maquina_to_venda=m,
                data_venda__gte=data_inicio
            ).aggregate(Sum('valor_venda'))['valor_venda__sum'] or 0
            
            m.total_gasto = total
            m.valor_disponivel = m.valor_limite - total
            
            if m.valor_limite > 0:
                m.porcentagem = (total / m.valor_limite) * 100
            else:
                m.porcentagem = 0
            
            m.porcentagem_barra = min(m.porcentagem, 100)

            if m.porcentagem >= 100:
                m.cor_barra = "#FF0000"
            elif m.porcentagem >= 80:
                m.cor_barra = "#CC4400"
            elif m.porcentagem > 50:
                m.cor_barra = "#FFFF66"
            else:
                m.cor_barra = "#28a745"

        return render(request, 'home.html', {'maquinas': maquinas})