# Requisitos do desafio

Deve se criar uma aplicação que permitirá a solicitação de um cartão de crédito, onde o usuário irá inserir suas informações básicas e o sistema irá fazer uma análise da liberação do cartão.

---------------------------------------------------------

# Solução


## Backend


O backend foi desenvolvido em Python utilizando o django rest framework, que permitirá a utilização dos métodos GET, POST e DELETE. Esta construção foi possível através do <em>serializer.py</em>:

<img src="api_rest2.png">

	class CartaoSerializer(serializers.ModelSerializer):

    		class Meta:
        		model = Cartao
        		fields = ('pk', 'nome','email','renda','pedido_em','pontuacao','aprovacao','credito')


Por outro lado, a Browsable API com o campo para inserção de dados foi construída no views.py:
	
	class CartaoListCreate(generics.ListCreateAPIView):
    		queryset = Cartao.objects.all()
    		serializer_class = CartaoSerializer
	class CartaoDetail(generics.RetrieveUpdateDestroyAPIView):
    		queryset = Cartao.objects.all()
    		serializer_class = CartaoSerializer 

O acesso à estas duas views, pode ser encontrada no arquivo <em>urls.py</em>:

	urlpatterns = [
    		path('api/cartao/', views.CartaoListCreate.as_view() ),
    		path('api/cartao/<int:pk>', views.CartaoDetail.as_view() ),
]

Os campos da nossa API (nome do usuário, renda etc), poderiam ser desenvolvidos de duas forma:

<ol>
<li>Diretamente no <em>serializer.py</em>; ou</li>
<li>No <em>models.py</em>;</li> 
</ol>

Eu optei pela segunda opção:

	class Cartao(models.Model):
    		nome = models.CharField("Nome", max_length = 200)
   		email = models.EmailField()
    		renda = models.CharField("Renda", blank=False, max_length=7)
		...

Os campos automáticos, editable=False :
		
		...
    		pontuacao = models.IntegerField("Pontuação", editable= False ,default= 0)#default
    		aprovacao = models.CharField("Cartão", editable=False, max_length= 15, default="Reprovado") 
    		credito = models.FloatField("Crédito", editable=False, default = 0)
    		pedido_em = models.DateTimeField("Pedido em", auto_now=True)

A regra de score do usuário e crédito:

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

-------------------------------------------------------------------------
# Frontend

O app cartaopedido que aparece em alguns arquivos é o que seria o frontend em React. Infelizmente, era necessário mais tempo para unir o front e o backend da aplicação. O cartaopedido foi criado através do comando:
         
         npm create-react-app cartaopedido
         
  
--------------------------------------------------------------------

# Desafios e Melhorias

<ol>
<li>Criar o frontend em React; </li>
<li> Deploy></li>
</ol>





         
