from rest_framework import routers

from order.views import OrderViewSet, OrderItemViewSet
from product.views import ProductViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'order-items', OrderItemViewSet, basename='order-items')
urlpatterns = router.urls