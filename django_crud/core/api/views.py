import pandas as pd
from rest_framework import views
from rest_framework import status
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = ShoeSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.validated_data, status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class FileUploadView(views.APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, resource=None,  *args, **kwargs):
        resource_dict = {
            'shoes': (ShoeSerializer, ['price',
                                       'discount',
                                       'size',
                                       'color',
                                       'shoes_stock',
                                       'shoes_bought',
                                       'shoe_model',
                                       'shoe_brand',
                                       'class_category']),

            'category': (CategorySerializer, ['category']),
        }
        resource = resource_dict.get(resource)

        if request.FILES.get('upload_file').name.endswith('.csv') and resource:

            df = pd.read_csv(request.FILES.get('upload_file'), delimiter=',').fillna(False)

            if isinstance(resource[0], ShoeSerializer):
                df['price'] = df['price'] * (1-df['discount'])

            if df.columns.to_list() == resource[1]:
                for index, row in df.iterrows():

                    data = {}

                    for i in resource[1]:

                        data[i] = row[i]

                        item = resource[0](data=data)

                        if item.is_valid():
                            item.save()

        return Response(status=status.HTTP_201_CREATED)
