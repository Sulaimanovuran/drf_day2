from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.decorators import action

from product.models import *
from .serializers import *


class ProductViewSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['GET'], detail=False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [i.name for i in cats]})

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Product.objects.all()[0:3]
        return Product.objects.filter(pk=pk)




















class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeatilAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer









class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductView(APIView):
#     def get(self, request):
#         return Response({'hello': 'John'})
