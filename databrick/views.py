from django.shortcuts import render
from rest_framework import generics,pagination
from .models import DatabrickModel
from .serializers import DatabrickSerializer
# Create your views here.

class DatabrickPagination(pagination.PageNumberPagination):
    page_size=500
    page_size_query_param="page_size"
    max_page_size=10000

class DatabrickListAPIView(generics.ListCreateAPIView):
    queryset=DatabrickModel.objects.all()
    serializer_class=DatabrickSerializer
    pagination_class=DatabrickPagination

class DatabrickCategoryListAPIView(generics.ListCreateAPIView):
    serializer_class=DatabrickSerializer
    pagination_class=DatabrickPagination
    def get_queryset(self):
        category=self.kwargs['category']
        queryset=DatabrickModel.objects.filter(category=category)
        return queryset


class DatabrickDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=DatabrickModel.objects.all()
    serializer_class=DatabrickSerializer
