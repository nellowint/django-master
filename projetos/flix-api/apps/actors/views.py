
from rest_framework import generics

from .models import Actor
from .serializers import ActorSerializer


class ActorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Actor.objects.filter(is_active=True)
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.filter(is_active=True)
    serializer_class = ActorSerializer
