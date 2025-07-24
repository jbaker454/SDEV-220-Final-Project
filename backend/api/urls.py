from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import user_list, ProductViewSet, ItemViewSet, ShipmentViewSet, ProcessViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'items', ItemViewSet)
router.register(r'shipments', ShipmentViewSet)
router.register(r'processes', ProcessViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
    path('users/', user_list),
]