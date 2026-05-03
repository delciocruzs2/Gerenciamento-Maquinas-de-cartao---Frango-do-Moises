from django.db import models
from django.utils import timezone
from maquinas.models import Maquinas_Model

class Vendas_Model(models.Model):
    id_venda = models.AutoField(primary_key=True)
    valor_venda = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    data_venda = models.DateField(default=timezone.now)
    comprovante = models.CharField(max_length=100, unique=True, null=True, blank=True)
    maquina_to_venda = models.ForeignKey(Maquinas_Model, on_delete=models.CASCADE,
                                         related_name='vendas', null=False, blank=False)
    
    class Meta:
        verbose_name = "Lançamento"
        verbose_name_plural = "Lançamentos"

