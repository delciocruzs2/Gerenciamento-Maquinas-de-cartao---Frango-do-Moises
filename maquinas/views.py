from django.shortcuts import render, redirect
from django.views import View
from maquinas.forms import *

class Maquina_View(View):
    def get(self, request) -> None:
        return render(request, template_name='gerenciador.html')
    

class Adicionar_Maquina_View(View):
    def get(self, request) -> None:
        form = Maquina_Form()
        return render(request, template_name='adicionar.html',
                      context={'form_adicionar':form})
    
    def post(self, request) -> redirect:
        form = Maquina_Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
        return render(request, 'adicionar.html', {'form_adicionar':form})