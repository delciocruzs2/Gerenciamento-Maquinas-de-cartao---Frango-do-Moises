from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.db.models import Sum

class Maquinas_Model(models.Model):
    id_maquina = models.AutoField(primary_key=True)
    nome_maquina = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name='Nome da Maquina')
    valor_limite_anual = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=1, 
        validators=[MinValueValidator(1), MaxValueValidator(1000000)],
        verbose_name='Limite anual'
    )
    valor_limite = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=False, 
        blank=False, 
        validators=[MaxValueValidator(100000)],
        verbose_name='Limite de gasto'
    )
    imagem_maquina = models.ImageField(upload_to='maquininhas', null=True, blank=True)
    dia_vencimento = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(31)],
        help_text="Escolha um dia entre 1 e 31 para o fechamento do ciclo."
    )

    def recalcular_limite(self):
        agora = timezone.now()
        ano_atual = agora.year
        mes_atual = agora.month
        total_gasto_ano = self.vendas.filter(data_venda__year=ano_atual).aggregate(Sum('valor_venda'))['valor_venda__sum'] or 0
        saldo_anual = self.valor_limite_anual - total_gasto_ano
        meses_restantes = 13 - mes_atual
        if meses_restantes > 0:
            novo_limite = saldo_anual / meses_restantes
            self.valor_limite = min(novo_limite, 100000)
        else:
            self.valor_limite = 0
        self.save()

    def save(self, *args, **kwargs):
        if not self.id_maquina:
            mes_atual = timezone.now().month
            meses_restantes = 13 - mes_atual
            calculo_inicial = self.valor_limite_anual / meses_restantes
            self.valor_limite = min(calculo_inicial, 100000)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nome_maquina
    
    class Meta:
        verbose_name = "Máquininha"
        verbose_name_plural = "Máquininhas"