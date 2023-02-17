from rest_framework import serializers
from .models import Collaborator

class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = ('id', 'name', 'surname', 'cellphone', 'dateofbirth', 'createdat')
        read_only_fields = ('createdat', )