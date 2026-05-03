from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from maquinas.forms import *
from maquinas.models import Maquinas_Model

class Maquina_View(View):
    def get(self, request):
        maquinas_cadastradas = Maquinas_Model.objects.all()
        return render(request, template_name='gerenciador.html', context={'maquinas': maquinas_cadastradas})

class Adicionar_Maquina_View(View):
    def get(self, request):
        form = Maquina_Form()
        return render(request, template_name='adicionar.html', context={'form_adicionar': form})
    
    def post(self, request):
        form = Maquina_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gerenciador_maquinas')
        return render(request, 'adicionar.html', {'form_adicionar': form})

class Atualizar_Maquina_View(View):
    def get(self, request, id):
        maquina = get_object_or_404(Maquinas_Model, id_maquina=id)
        form = Maquina_Form(instance=maquina)
        return render(request, template_name='atualizar.html', context={'form_atualizar': form, 'maquina': maquina})
    
    def post(self, request, id):
        maquina = get_object_or_404(Maquinas_Model, id_maquina=id)
        form = Maquina_Form(request.POST, request.FILES, instance=maquina)
        if form.is_valid():
            maquina = form.save()
            maquina.recalcular_limite()
            return redirect('gerenciador_maquinas')
        return render(request, 'atualizar.html', {'form_atualizar': form, 'maquina': maquina})

class Deletar_Maquina_View(View):
    def get(self, request, id: int):
        objeto_escolhido = get_object_or_404(Maquinas_Model, id_maquina=id)
        objeto_escolhido.delete()
        return redirect('gerenciador_maquinas')