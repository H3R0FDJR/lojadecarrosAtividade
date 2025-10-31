from django.shortcuts import render


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Carro

class CarroListView(ListView):
    model = Carro
    template_name = 'loja/listar.html'  
    context_object_name = 'carros'      

class CarroDetailView(DetailView):
    model = Carro
    template_name = 'loja/detalhe.html'

class CarroCreateView(CreateView):
    model = Carro
    fields = ['marca', 'modelo', 'ano', 'preco', 'descricao']
    template_name = 'loja/form.html'   

class CarroUpdateView(UpdateView):
    model = Carro
    fields = ['marca', 'modelo', 'ano', 'preco', 'descricao']
    template_name = 'loja/form.html'    

class CarroDeleteView(DeleteView):
    model = Carro
    template_name = 'loja/confirm_delete.html' 
    success_url = reverse_lazy('carro_listar') 