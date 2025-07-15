from rest_framework import viewsets
from .models import Resource, Shipment, Process, Order, Location, Transaction
from .serializers import (
    ResourceSerializer, ShipmentSerializer, ProcessSerializer,
    OrderSerializer, LocationSerializer, TransactionSerializer
)

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer