from rest_framework import routers
from .api import CollaboratorViewSet

router = routers.DefaultRouter()

router.register('api/collaborators', CollaboratorViewSet, 'collaborators')

urlpatterns = router.urls