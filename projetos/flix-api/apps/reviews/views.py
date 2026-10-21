
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import CustomPermissions
from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions, )
    queryset = Review.objects.filter(is_active=True)
    serializer_class = ReviewSerializer

class ReviewListRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions, )
    queryset = Review.objects.filter(is_active=True)
    serializer_class = ReviewSerializer
