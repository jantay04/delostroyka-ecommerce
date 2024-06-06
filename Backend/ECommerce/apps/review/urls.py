from rest_framework import routers

from apps.review.views import ReviewViewSet

router = routers.SimpleRouter()

router.register(r'reviews', ReviewViewSet, basename='reviews')

urlpatterns = router.urls
