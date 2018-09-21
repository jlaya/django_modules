from .models import Products
from .serializers import ProductsListSerializer
from .serializers import ProductsDetailSerializer
from .serializers import ProductsCreateUpdateSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import DestroyAPIView


class ProductsListAPI(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializer

class ProductsDetailAPI(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializer

class ProductsCreateAPI(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsCreateUpdateSerializer

class ProductsUpdateAPI(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsCreateUpdateSerializer

class ProductsDeleteAPI(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializer