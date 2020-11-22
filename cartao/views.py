from django.shortcuts import render
from .models import Cartao
from .serializers import CartaoSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Cartao
from .serializers import *

#vamos lidar com o GET e o POST
class CartaoListCreate(generics.ListCreateAPIView):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer
class CartaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

