
from rest_framework import generics, permissions

from .models import Actor
from .serializers import ActorSerializer


class ActorListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Actor.objects.filter(is_active=True)
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Actor.objects.filter(is_active=True)
    serializer_class = ActorSerializer
