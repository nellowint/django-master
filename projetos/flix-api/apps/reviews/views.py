
from rest_framework import generics, permissions

from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Review.objects.filter(is_active=True)
    serializer_class = ReviewSerializer

class ReviewListRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Review.objects.filter(is_active=True)
    serializer_class = ReviewSerializer
