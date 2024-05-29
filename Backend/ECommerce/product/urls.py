from rest_framework import routers

from product.views import ProductViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')
urlpatterns = router.urls