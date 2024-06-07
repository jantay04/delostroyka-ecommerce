from rest_framework import routers

from api.product.views import ProductViewSet, CategoryViewSet, ProductImageViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'product-images', ProductImageViewSet, basename='product-images')

urlpatterns = router.urls