
from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieListCreateAPIView.as_view(), name='movie_view'),
    path('<int:pk>/', views.MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie_detail'),
    path('stats/', views.MovieStatsView.as_view(), name='movie_stats'),
]