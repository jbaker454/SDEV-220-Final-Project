from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ResourceViewSet, ShipmentViewSet, ProcessViewSet,
    OrderViewSet, LocationViewSet, TransactionViewSet
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
]