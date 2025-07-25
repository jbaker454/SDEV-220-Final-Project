from rest_framework import serializers
from .models import User, Product, Item, Shipment, Process, Order, Location, Transaction

class UserSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_str_representation(self, obj):
        return str(obj)

class ItemSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'quantity', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)

class ShipmentSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Shipment
        fields = ['id', 'item', 'quantity', 'type', 'date', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)

class ProcessSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Process
        fields = ['id', 'name', 'description', 'item', 'status', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)

class OrderSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'item', 'quantity', 'date', 'status', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)

class LocationSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['id', 'name', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)

class ProductSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'quantity', 'location', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)

class TransactionSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['id', 'product', 'quantity_change', 'timestamp', 'reason', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)
