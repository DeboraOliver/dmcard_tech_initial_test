from rest_framework import serializers
from .models import Cartao


class CartaoSerializer(serializers.ModelSerializer):

    pontuacao = serializers.CharField(source = 'cartao.pontuacao')#default
    aprovado = serializers.CharField( source = 'cartao.aprovacao') #default
    credito = serializers.CharField(source = 'cartao.credito')

    class Meta:
        model = Cartao
        #exclude = ()
        fields = ('pk', 'nome','email','renda','pedido_em','pontuacao','aprovado','credito')