from rest_framework.serializers import ModelSerializer

from .models import Utilisateur


class FormationSerializer(ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = "__all__"