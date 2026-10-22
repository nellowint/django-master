
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import CustomPermissions

from .models import Review
from .serializers import ReviewModelSerializer, ReviewSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions,)
    queryset = Review.objects.filter(is_active=True)

    def get_serializer_class(self):
        return (
            ReviewSerializer
            if self.request.method == 'GET'
            else ReviewModelSerializer
        )


class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions,)
    queryset = Review.objects.filter(is_active=True)

    def get_serializer_class(self):
        return (
            ReviewSerializer
            if self.request.method == 'GET'
            else ReviewModelSerializer
        )
