from django.db import models
from django.utils import timezone

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Supplier(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20,null=True)
    country = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    zip = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=20,null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Item(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    suppliers = models.ManyToManyField(Supplier, related_name='items',blank=True)

    def __str__(self):
        return self.name

class Supply(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='supplies')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplies')
    quantity = models.IntegerField()
    date_supplied = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.item.quantity += self.quantity
        self.item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} of {self.item.name} supplied by {self.supplier.name} on {self.date_supplied}"