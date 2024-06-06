from rest_framework import routers

from apps.cart.views import CartViewSet, CartItemViewSet

router = routers.SimpleRouter()
router.register(r'carts', CartViewSet, basename='carts')
router.register(r'cart-items', CartItemViewSet, basename='cart-items')
urlpatterns = router.urls