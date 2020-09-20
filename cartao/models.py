from django.db import models
#from .utils import pontuacao_credito,aprovacao

def pontuacao_credito(self):
    pass


class Cartao(models.Model):
    nome = models.CharField("Nome", max_length = 200)
    email = models.EmailField()
    renda = models.IntegerField("Renda", blank=False)
    #pontuacao = models.CharField("pontuacao",max_length=3, editable= False ,default= pontuacao_credito(self))#default
    #aprovado = models.BooleanField("aprovado",editable=False, default= aprovacao(self)) #default
    #credito = models.FloatField("credito", editable=False)
    pedido_em = models.DateTimeField("pedido_em", auto_now_add=True)

    def pontuacao(self):
        "Pontuação "
        import random
        self.pontuacao_credito = random.randint (1, 999)
        return self.pontuacao_credito

    def aprovacao(self):
        "Cartão "
        if int (self.pontuacao_credito) <= 299:
            return "Não Aprovado"
        else:
            return "Aprovado"

    def credito_dado(self):
        "Crédito do cliente"
        if int (self.pontuacao_credito) <= 299:
            return 0 * self.renda
        elif (int (self.pontuacao_credito) >= 300) and (int (self.pontuacao_credito) <= 599):
            return 1000
        elif (int (self.pontuacao_credito) >= 600) and (int (self.pontuacao_credito) <= 799):
            return self.renda * (1 + 0.5)
        elif (int (self.pontuacao_credito) >= 800) and (int (self.pontuacao_credito) <= 950):
            return 2 * self.renda
        else:
            return 1000000

    def __str__(self):
        return self.nome



