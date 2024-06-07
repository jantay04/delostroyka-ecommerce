from rest_framework import routers

from api.order.views import OrderViewSet, OrderItemViewSet

router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'order-items', OrderItemViewSet, basename='order-items')
urlpatterns = router.urls