
from rest_framework import generics, permissions

from .models import Genre
from .serializers import GenreSerializer


class GenreListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Genre.objects.filter(is_active=True)
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Genre.objects.filter(is_active=True)
    serializer_class = GenreSerializer
