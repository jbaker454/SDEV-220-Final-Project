from rest_framework import serializers
from .models import Resource, Shipment, Process, Order, Location, Transaction

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'