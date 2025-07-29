from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ResourceViewSet,
    ShipmentViewSet,
    ProcessViewSet,
    OrderViewSet,
    LocationViewSet,
    TransactionViewSet,
    user_list,  # Include this only if your project still uses a user endpoint
)

router = DefaultRouter()
router.register(r'resources', ResourceViewSet)
router.register(r'shipments', ShipmentViewSet)
router.register(r'processes', ProcessViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', user_list),  # Remove this line if you no longer use `user_list`
]
