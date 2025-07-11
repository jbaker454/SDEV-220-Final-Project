from django.db import models
from django.contrib.auth.models import User 

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)


class Shipment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    type = models.CharField(max_length=10, choices=[('IN', 'Incoming'), ('OUT', 'Outgooing')])
    date = models.TimeField(auto_now_add=True)

class Process(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, 
        choices=[
            ('pending', 'Pending'),
            ('done', 'Done'),
            ],
            default='pending'
        )

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="processing")

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_change = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255, help_text="e.g. Received, Shipped, Spoiled")

    def __str__(self):
        return f"{self.reason} {self.quantity_change} of {self.product.name}"
