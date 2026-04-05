from django.shortcuts import render, redirect
from django.views import View
from maquinas.forms import *

class Maquina_View(View):
    def get(self, request) -> None:
        return render(request, template_name='gerenciador.html')
    
