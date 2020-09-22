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


# @api_view (['GET', 'POST'])
# def cartao_list(request):
#     if request.method == 'GET':
#         data = Cartao.objects.all ()
#
#         serializer = CartaoSerializer (data, context={'request': request}, many=True)
#
#         return Response (serializer.data)
#
#     elif request.method == 'POST':
#         serializer = CartaoSerializer (data=request.data)
#         if serializer.is_valid ():
#             serializer.save ()
#             return Response (status=status.HTTP_201_CREATED)
#
#         return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view (['PUT', 'DELETE'])
# def cartao_detail(request, pk):
#     try:
#         cartao = Cartao.objects.get (pk=pk)
#     except Cartao.DoesNotExist:
#         return Response (status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         serializer = CartaoSerializer (cartao, data=request.data, context={'request': request})
#         if serializer.is_valid ():
#             serializer.save ()
#             return Response (status=status.HTTP_204_NO_CONTENT)
#         return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         Cartao.delete ()
#         return Response (status=status.HTTP_204_NO_CONTENT)
#
