from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    received_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='resources')

    def __str__(self):
        return self.name

class Shipment(models.Model):
    SHIPMENT_TYPE_CHOICES = [
        ('IN', 'Incoming'),
        ('OUT', 'Outgoing'),
    ]

    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='shipments')
    quantity = models.IntegerField()
    shipment_type = models.CharField(max_length=10, choices=SHIPMENT_TYPE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.shipment_type} {self.quantity} of {self.resource.name} on {self.date}"


class Process(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='processes')
    items_per_second = models.FloatField(default=1.0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.name} ({self.status})"


class Order(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')

    def __str__(self):
        return f"Order of {self.quantity} {self.resource.name} ({self.status})"



class Transaction(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='transactions')
    quantity_change = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255, help_text="e.g. Received, Shipped, Spoiled")

    def __str__(self):
        return f"{self.reason} {self.quantity_change} of {self.resource.name}"