from django.db import models


class candle(models.Model):

    moeda = models.CharField(max_length=200)
    periodicidade = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    entrada = models.DecimalField(max_digits=20, decimal_places=8)
    maior = models.DecimalField(max_digits=20, decimal_places=8)
    menor = models.DecimalField(max_digits=20, decimal_places=8)
    saida = models.DecimalField(max_digits=20, decimal_places=8)


