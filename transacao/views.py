from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Sum
from datetime import date
from transacao.forms import Vendas_Form
from transacao.models import Vendas_Model
from maquinas.models import Maquinas_Model

class Vendas_View(View):
    def get(self, request):
        form_venda = Vendas_Form()
        ultimas_vendas = Vendas_Model.objects.all().order_by('-id_venda')[:10]
        return render(request, template_name='lancamento.html',
                      context={'form_venda': form_venda, 'ultimas_vendas': ultimas_vendas})

    def post(self, request):
        form_venda = Vendas_Form(request.POST)
        if form_venda.is_valid():
            form_venda.save()
            return redirect(request.path)
        
        ultimas_vendas = Vendas_Model.objects.all().order_by('-id_venda')[:10]
        return render(request, template_name='lancamento.html',
                      context={'form_venda': form_venda, 'ultimas_vendas': ultimas_vendas})

class Financeiro_Maquina_View(View):
    def get(self, request, maquina_id):
        maquina = get_object_or_404(Maquinas_Model, pk=maquina_id)
        hoje = date.today()
        
        # 1. CÁLCULO ACUMULADO NO ANO ATUAL
        total_ano = Vendas_Model.objects.filter(
            maquina_to_venda=maquina,
            data_venda__year=hoje.year
        ).aggregate(Sum('valor_venda'))['valor_venda__sum'] or 0
        
        saldo_anual_restante = maquina.valor_limite_anual - total_ano
        
        # 2. LIMITE MENSAL RECALCULADO
        meses_restantes = 13 - hoje.month
        if meses_restantes > 0:
            limite_dinamico = saldo_anual_restante / meses_restantes
            limite_mensal_atual = max(min(limite_dinamico, 100000), 0)
        else:
            limite_mensal_atual = 0

        # 3. LANÇADO NO MÊS (Ciclo de Vencimento)
        if hoje.day < maquina.dia_vencimento:
            mes_ini = hoje.month - 1 if hoje.month > 1 else 12
            ano_ini = hoje.year if hoje.month > 1 else hoje.year - 1
            data_inicio_mes = date(ano_ini, mes_ini, maquina.dia_vencimento)
        else:
            data_inicio_mes = date(hoje.year, hoje.month, maquina.dia_vencimento)

        total_mes = Vendas_Model.objects.filter(
            maquina_to_venda=maquina,
            data_venda__gte=data_inicio_mes
        ).aggregate(Sum('valor_venda'))['valor_venda__sum'] or 0

        # 4. DISPONÍVEL NO MÊS (NOVO)
        disponivel_mes = limite_mensal_atual - total_mes

        # 5. BUSCA DE VENDAS PARA A TABELA
        vendas = Vendas_Model.objects.filter(maquina_to_venda=maquina).order_by('-data_venda')
        
        return render(request, 'financeiro.html', {
            'maquina': maquina,
            'vendas': vendas,
            'total_ano': total_ano,
            'saldo_anual_restante': saldo_anual_restante,
            'limite_mensal_atual': limite_mensal_atual,
            'total_mes': total_mes,
            'disponivel_mes': disponivel_mes  # Enviando para o HTML
        })
    
class Venda_Update_View(UpdateView):
    model = Vendas_Model
    fields = ['comprovante', 'valor_venda', 'data_venda']
    template_name = 'editar_venda.html'
    
    def get_success_url(self):
        return reverse_lazy('financeiro_maquina', kwargs={'maquina_id': self.object.maquina_to_venda.pk})

def excluir_venda_view(request, pk):
    venda = get_object_or_404(Vendas_Model, pk=pk)
    maquina_id = venda.maquina_to_venda.pk
    venda.delete()
    return redirect('financeiro_maquina', maquina_id=maquina_id)