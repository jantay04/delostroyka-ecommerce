from rest_framework import routers

from .views import ProviderViewSet

router = routers.SimpleRouter()
router.register(r'providers', ProviderViewSet, basename='providers')

urlpatterns = router.urls