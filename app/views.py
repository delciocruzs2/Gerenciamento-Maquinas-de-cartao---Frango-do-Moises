from django.shortcuts import render, redirect
from django.views import View

class Home_View(View):
    def get(self, request) -> None:
        return render(request, template_name='base.html')