
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import CustomPermissions

from .models import Actor
from .serializers import ActorSerializer


class ActorListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions, )
    queryset = Actor.objects.filter(is_active=True)
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions, )
    queryset = Actor.objects.filter(is_active=True)
    serializer_class = ActorSerializer
