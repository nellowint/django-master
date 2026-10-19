
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ActorListCreateAPIView.as_view(), name='view_actors'),
    path('<int:pk>/', views.ActorRetrieveUpdateDestroyAPIView.as_view(), name='detail_actors')
]