from rest_framework.serializers import ModelSerializer
from .models import Products


class ProductsListSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = (
                  'id',
                  'name',
                  'quantity',
                  'price',
                  'description',
                  'picture'
                  )

class ProductsDetailSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = (
                  'id',
                  'name',
                  'quantity',
                  'price',
                  'description',
                  'picture'
                  )


class ProductsCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = (
                  'name',
                  'quantity',
                  'price',
                  'description'
                  )