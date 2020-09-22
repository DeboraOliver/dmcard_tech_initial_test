from rest_framework import serializers
from .models import Cartao


class CartaoSerializer(serializers.ModelSerializer):

    #pontuacao = serializers.ReadOnlyField(source = 'cartao.pontuacao')#default
    #aprovado = serializers.ReadOnlyField( source = 'cartao.aprovacao') #default
    #credito = serializers.ReadOnlyField(source = 'cartao.credito')

    class Meta:
        model = Cartao
        #exclude = ()
        fields = ('pk', 'nome','email','renda','pedido_em','pontuacao','aprovacao','credito')

