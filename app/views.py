from django.views import View
from django.shortcuts import render
from django.db.models import Sum
from datetime import date
from maquinas.models import Maquinas_Model
from transacao.models import Vendas_Model

class Home_View(View):
    def get(self, request):
        maquinas = Maquinas_Model.objects.all()
        hoje = date.today()
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
                 "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        
        for m in maquinas:
            # 1. CÁLCULO DO LIMITE MENSAL DINÂMICO
            # Soma tudo o que foi gasto no ano até agora (Jan até hoje)
            total_ano = Vendas_Model.objects.filter(
                maquina_to_venda=m,
                data_venda__year=hoje.year
            ).aggregate(Sum('valor_venda'))['valor_venda__sum'] or 0
            
            saldo_anual_restante = m.valor_limite_anual - total_ano
            meses_restantes = 13 - hoje.month # Ex: Maio é 5, sobra 13-5 = 8 meses
            
            # Define o limite mensal dinamicamente para exibição
            if meses_restantes > 0:
                limite_dinamico = saldo_anual_restante / meses_restantes
                # Garante que o limite não seja negativo e respeite o teto de 100k do seu validador
                m.valor_limite_calculado = max(min(limite_dinamico, 100000), 0)
            else:
                m.valor_limite_calculado = 0

            # 2. DEFINIÇÃO DO CICLO MENSAL (Datas)
            if hoje.day < m.dia_vencimento:
                mes_inicio = hoje.month - 1 if hoje.month > 1 else 12
                ano_inicio = hoje.year if hoje.month > 1 else hoje.year - 1
                data_inicio = date(ano_inicio, mes_inicio, m.dia_vencimento)
                m.vencimento_completo = f"{m.dia_vencimento} de {meses[hoje.month - 1]}"
            else:
                data_inicio = date(hoje.year, hoje.month, m.dia_vencimento)
                prox_mes_idx = hoje.month if hoje.month < 12 else 0
                m.vencimento_completo = f"{m.dia_vencimento} de {meses[prox_mes_idx]}"

            # 3. CÁLCULO DOS LANÇAMENTOS DO MÊS ATUAL
            total_mes = Vendas_Model.objects.filter(
                maquina_to_venda=m,
                data_venda__gte=data_inicio
            ).aggregate(Sum('valor_venda'))['valor_venda__sum'] or 0
            
            m.total_gasto = total_mes
            m.valor_disponivel = m.valor_limite_calculado - total_mes
            
            # 4. PORCENTAGEM E CORES (Baseado no limite calculado)
            if m.valor_limite_calculado > 0:
                m.porcentagem = (total_mes / m.valor_limite_calculado) * 100
            else:
                m.porcentagem = 100 if total_mes > 0 else 0
            
            m.porcentagem_barra = min(m.porcentagem, 100)
            
            if m.porcentagem >= 100:
                m.cor_barra = "#FF0000"
            elif m.porcentagem >= 80:
                m.cor_barra = "#CC4400"
            else:
                m.cor_barra = "#28a745"

            # 5. DADOS ANUAIS PARA O CARD
            m.disponivel_anual = saldo_anual_restante
            m.porcentagem_anual = (total_ano / m.valor_limite_anual * 100) if m.valor_limite_anual > 0 else 0
            m.porcentagem_anual_barra = min(m.porcentagem_anual, 100)

        return render(request, 'home.html', {'maquinas': maquinas})