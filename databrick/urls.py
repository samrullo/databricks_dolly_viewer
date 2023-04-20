from django.urls import path
from .views import DatabrickListAPIView,DatabrickDetailAPIView,DatabrickCategoryListAPIView
from .datasets_view import DatabrickContextAPIView

urlpatterns=[
    path('<int:pk>',DatabrickDetailAPIView.as_view()),
    path('<str:category>',DatabrickCategoryListAPIView.as_view()),
    path('with_context',DatabrickContextAPIView.as_view()),
    path('',DatabrickListAPIView.as_view())
]