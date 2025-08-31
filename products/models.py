from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)
    
class User(AbstractUser):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Manager", "Manager"),
        ("Cashier", "Cashier"),
        ("Waiter", "Waiter"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Waiter")
    
    def __str__(self):
        return f"{self.username} ({self.role})"