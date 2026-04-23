from django.contrib import admin
from django.urls import path, include
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',Home_View.as_view(), name='home'),
    path('v1/maquinas/', include('maquinas.urls')),
    path('v1/transacao/', include('transacao.urls') )

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)