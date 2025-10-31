from django.urls import path
from .views import (
    CarroListView,
    CarroDetailView,
    CarroCreateView,
    CarroUpdateView,
    CarroDeleteView
)

urlpatterns = [
    path('', CarroListView.as_view(), name='carro_listar'),
    path('carro/<int:pk>/', CarroDetailView.as_view(), name='carro_detalhe'),
    path('carro/novo/', CarroCreateView.as_view(), name='carro_novo'),
    path('carro/<int:pk>/editar/', CarroUpdateView.as_view(), name='carro_editar'),
    path('carro/<int:pk>/deletar/', CarroDeleteView.as_view(), name='carro_deletar'),
]