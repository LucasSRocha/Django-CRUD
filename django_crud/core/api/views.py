from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Shoes
from core.models import Categories

from .serializers import ShoeSerializer
from .serializers import CategorySerializer
from django_filters import rest_framework as filters

number_filters = ['lt', 'gt', 'gte', 'lte', 'exact', 'range']

char_filters = ['icontains', 'exact']


class CategoryApiView(viewsets.ModelViewSet):

    queryset = Categories.objects.all()

    serializer_class = CategorySerializer


class ShoesFilter(filters.FilterSet):
    class Meta:
        model = Shoes
        fields = {
            'price': number_filters,
            'size': number_filters,
            'color': char_filters,
            'shoe_brand': char_filters,
            'shoe_model': char_filters,
            'class_category': ['exact'],
                  }


class ShoesApiView(viewsets.ModelViewSet):

    queryset = Shoes.objects.all()

    serializer_class = ShoeSerializer

    filterset_class = ShoesFilter
