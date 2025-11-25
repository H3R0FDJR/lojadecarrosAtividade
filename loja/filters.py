import django_filters
from django.db.models import Q
from .models import Carro 

class CarroFilter(django_filters.FilterSet):
    busca = django_filters.CharFilter(
        method='filter_busca', 
        label='Buscar Marca ou Modelo'
    )
    
    ano = django_filters.NumberFilter(
        field_name='ano', 
        lookup_expr='exact', 
        label='Ano modelo'
    )

    class Meta:
        model = Carro
    
        fields = ['ano'] 
        
    def filter_busca(self, queryset, name, value):
        return queryset.filter(
            Q(marca__icontains=value) | Q(modelo__icontains=value)
        )