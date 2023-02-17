from .models import Collaborator
from rest_framework import permissions
from .serializers import CollaboratorSerializer
from rest_framework.viewsets import ModelViewSet


class CollaboratorViewSet(ModelViewSet):
    queryset = Collaborator.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = CollaboratorSerializer