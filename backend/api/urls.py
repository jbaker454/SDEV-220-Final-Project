from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import user_list, ProductViewSet, ItemViewSet, ShipmentViewSet, ProcessViewSet, OrderViewSet
=======
from .views import (
    ResourceViewSet, ShipmentViewSet, ProcessViewSet,
    OrderViewSet, LocationViewSet, TransactionViewSet
)
>>>>>>> 44aa1c70a9aa4ad66f463bbac37093c14572f3c6

router = DefaultRouter()
router.register(r'resources', ResourceViewSet)
router.register(r'shipments', ShipmentViewSet)
router.register(r'processes', ProcessViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
<<<<<<< HEAD
    path('', include(router.urls)),  # Include the router's URLs
    path('users/', user_list),
=======
    path('', include(router.urls)),
>>>>>>> 44aa1c70a9aa4ad66f463bbac37093c14572f3c6
]