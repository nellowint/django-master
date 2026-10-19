
from rest_framework import generics

from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.filter(is_active=True)
    serializer_class = ReviewSerializer

class ReviewListRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.filter(is_active=True)
    serializer_class = ReviewSerializer
