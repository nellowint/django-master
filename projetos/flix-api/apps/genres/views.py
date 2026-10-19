
from rest_framework import generics

from .models import Genre
from .serializers import GenreSerializer


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.filter(is_active=True)
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.filter(is_active=True)
    serializer_class = GenreSerializer
