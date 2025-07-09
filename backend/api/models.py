from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
