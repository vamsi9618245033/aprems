from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.IntegerField()
    password1=models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.subject


from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    price = models.IntegerField()
    CAT_CHOICES = (
        ('Vegetable', 'Vegetable'),
        ('Fruit', 'Fruit'),
        ('Seeds', 'Seeds'),
        ('Others', 'Others'),
    )
    category = models.CharField(max_length=100, choices=CAT_CHOICES)  # Corrected field name
    location = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add a foreign key field to associate products with users

    def __str__(self):
        return self.name





from django.db import models
from django.contrib.auth.models import User
from .models import Product  # Import your Product model

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


# models.py
from django.db import models

class Payment(models.Model):
    order_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as needed

