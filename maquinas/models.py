from django.db import models

class Maquinas_Model(models.Model):
    id_maquina = models.AutoField(primary_key=True)
    nome_maquina = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name='Nome da Maquina')
    valor_limite = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Limite de gasto')
    imagem_maquina = models.ImageField(upload_to='maquininhas', null=True, blank=True)

    def __str__(self) -> str:
        return self.nome_maquina