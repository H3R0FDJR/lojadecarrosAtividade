from django.db import models
from django.urls import reverse

class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

    def get_absolute_url(self):
        return reverse('carro_detalhe', kwargs={'pk': self.pk})