<<<<<<< HEAD
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import User, Product, Item, Shipment, Process, Order
from .serializers import UserSerializer, ProductSerializer, ItemSerializer, ShipmentSerializer, ProcessSerializer, OrderSerializer
from django.shortcuts import get_object_or_404
=======
from rest_framework import viewsets
from .models import Resource, Shipment, Process, Order, Location, Transaction
from .serializers import (
    ResourceSerializer, ShipmentSerializer, ProcessSerializer,
    OrderSerializer, LocationSerializer, TransactionSerializer
)
>>>>>>> 44aa1c70a9aa4ad66f463bbac37093c14572f3c6

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

<<<<<<< HEAD
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
=======
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
>>>>>>> 44aa1c70a9aa4ad66f463bbac37093c14572f3c6
