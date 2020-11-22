from django.db import models
from datetime import datetime


class Cartao(models.Model):
    nome = models.CharField("Nome", max_length = 200)
    email = models.EmailField()
    cpf = models.CharField("CPF",max_length = 15)
    renda = models.CharField("Renda", blank=False, max_length=7)
    pontuacao = models.IntegerField("Pontuação", editable= False ,default= 0)#default
    aprovacao = models.CharField("Cartão", editable=False, max_length= 15, default="Reprovado") #default
    credito = models.FloatField("Crédito", editable=False, default = 0)
    pedido_em = models.DateTimeField("Pedido em", auto_now=True)



    def save(self, *args, **kwargs):
        import random
        self.pontuacao = random.randint (1, 999)
        if int(self.pontuacao <= 299):
            self.aprovacao = "Reprovado"
            self.credito = 0
        else:
            self.aprovacao = "Aprovado"
            if (int (self.pontuacao) >= 300) and (int (self.pontuacao) <= 599):
                self.credito = 1000
            elif (int (self.pontuacao) >= 600) and (int (self.pontuacao) <= 799):
                self.credito = int(self.renda) * (1 + 0.5)
            elif (int (self.pontuacao) >= 800) and (int (self.pontuacao) <= 950):
                self.credito = 2 * int (self.renda)
            else:
                self.credito = 1000000
        super ().save (*args, **kwargs)

		
    def get_pedido_em(self):
        return self.pedido_em.strftime('%Y-%m-%dT%H:%M')

    def __str__(self):
        return self.nome





