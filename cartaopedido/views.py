from django.shortcuts import render


def index(request):
    return render(request, 'cartaopedido/src/App.js')