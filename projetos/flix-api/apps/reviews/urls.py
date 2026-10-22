
from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.ReviewListCreateAPIView.as_view(),
        name='review_view'
    ),
    path(
        '<int:pk>/',
        views.ReviewRetrieveUpdateDestroyAPIView.as_view(),
        name='review_detail'
    )
]
