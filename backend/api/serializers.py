from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Resource, Shipment, Process, Order, Location, Transaction


class UserSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_str_representation(self, obj):
        return str(obj)


class ResourceSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Resource
        fields = ['id', 'name', 'description', 'quantity', 'received_date', 'location', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)


class ShipmentSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Shipment
        fields = ['id', 'resource', 'quantity', 'shipment_type', 'date', 'completed', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)


class ProcessSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Process
        fields = ['id', 'name', 'description', 'resource', 'items_per_second', 'status', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)


class OrderSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'resource', 'quantity', 'date', 'status', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)


class LocationSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['id', 'name', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)


class TransactionSerializer(serializers.ModelSerializer):
    str_representation = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['id', 'resource', 'quantity_change', 'timestamp', 'reason', 'str_representation']

    def get_str_representation(self, obj):
        return str(obj)
