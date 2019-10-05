from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Shoes
from core.models import Categories

from .serializers import ShoeSerializer
from .serializers import CategorySerializer


class CategoryApiView(viewsets.ModelViewSet):

    queryset = Categories.objects.all()

    serializer_class = CategorySerializer


class ShoesApiView(viewsets.ModelViewSet):

    queryset = Shoes.objects.all()

    serializer_class = ShoeSerializer
