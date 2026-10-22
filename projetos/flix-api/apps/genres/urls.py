
from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.GenreListCreateAPIView.as_view(),
        name='view_genres'
    ),
    path(
        '<int:pk>/',
        views.GenreRetrieveUpdateDestroyAPIView.as_view(),
        name='detail_genres'
    )
]
