from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from transacao.forms import *
from transacao.models import *

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
        vendas = Vendas_Model.objects.filter(maquina_to_venda=maquina).order_by('-data_venda')
        
        return render(request, 'financeiro.html', {
            'maquina': maquina,
            'vendas': vendas
        })
    
class Venda_Update_View(UpdateView):
    model = Vendas_Model
    form_class = Vendas_Form
    template_name = 'editar_venda.html'
    
    def get_success_url(self):
        return reverse_lazy('financeiro_maquina', kwargs={'maquina_id': self.object.maquina_to_venda.pk})

def excluir_venda_view(request, pk):
    venda = get_object_or_404(Vendas_Model, pk=pk)
    maquina_id = venda.maquina_to_venda.pk
    venda.delete()
    return redirect('financeiro_maquina', maquina_id=maquina_id)