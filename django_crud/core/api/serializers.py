from rest_framework import serializers

from core.models import Shoes
from core.models import Categories


class CategorySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Categories.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

    class Meta:
        model = Categories

        fields = ['category']


class ShoeSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        categories = validated_data.pop('class_category')

        instace = Shoes.objects.create(**validated_data)

        instace.class_category.set(categories)

        return instace

    def update(self, instance, validated_data):

        instance.size = validated_data.get('size', instance.size)

        instance.color = validated_data.get('color', instance.color)

        instance.price = validated_data.get('price', instance.price)

        instance.shoe_model = validated_data.get('shoe_model', instance.shoe_model)

        instance.shoes_stock = validated_data.get('shoes_stock', instance.shoes_stock)

        instance.shoes_bought = validated_data.get('shoes_bought', instance.shoes_bought)

        instance.shoe_brand = validated_data.get('shoe_brand', instance.shoe_brand)

        instance.save()

        instance.class_category.set(validated_data.get('class_category', instance.class_category))

        return instance

    class Meta:
        model = Shoes
        fields = '__all__'

        required = [
            'price',
            'color',
            'shoe_model',
            'size',
            'shoe_stock',
        ]
        read_only_fields = ['id', ]
