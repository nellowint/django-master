
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import CustomPermissions

from .models import Genre
from .serializers import GenreSerializer


class GenreListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions, )
    queryset = Genre.objects.filter(is_active=True)
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions, )
    queryset = Genre.objects.filter(is_active=True)
    serializer_class = GenreSerializer
