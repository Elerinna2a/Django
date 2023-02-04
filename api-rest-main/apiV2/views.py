from rest_framework.viewsets import ModelViewSet

from .models import Utilisateur
from .serializers import FormationSerializer as UtilisateurSerializer

# Create your views here.

class UtilisateurViewSet(ModelViewSet):
   queryset = Utilisateur.objects.all()
   serializer_class = UtilisateurSerializer
   filterset_fields = ['is_admin']
   search_fields = ['nom']
        