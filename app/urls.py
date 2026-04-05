from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home_View.as_view(), name='home'),
    path('v1/maquinas/', include('maquinas.urls')),

]
