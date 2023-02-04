from rest_framework.serializers import ModelSerializer

from .models import Formation


class FormationSerializer(ModelSerializer):
    class Meta:
        model = Formation
        fields = "__all__"