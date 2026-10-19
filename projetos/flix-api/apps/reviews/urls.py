
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewListCreateAPIView.as_view(), name='review_view'),
    path('<int:pk>/', views.ReviewListRetrieveUpdateDestroyAPIView.as_view(), name='review_detail')
]