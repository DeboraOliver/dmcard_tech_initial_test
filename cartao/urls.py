from django.urls import path
from . import views

urlpatterns = [
    path('api/cartao/', views.CartaoListCreate.as_view() ),
    path('api/cartao/<int:pk>', views.CartaoDetail.as_view() ),
]