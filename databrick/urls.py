from django.urls import path
from .views import DatabrickListAPIView,DatabrickDetailAPIView,DatabrickCategoryListAPIView

urlpatterns=[
    path('<int:pk>',DatabrickDetailAPIView.as_view()),
    path('<str:category>',DatabrickCategoryListAPIView.as_view()),
    path('',DatabrickListAPIView.as_view())
]