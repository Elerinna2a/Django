from rest_framework import routers

from .views import UtilisateurViewSet

router = routers.DefaultRouter()
router.register('utilisateurs', UtilisateurViewSet)