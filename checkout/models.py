from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from product.models import Product

class Order(models.Model):
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    address_line_1 = models.CharField(max_length=100, blank=False)
    address_line_2 = models.CharField(max_length=100, blank=True)
    address_line_3 = models.CharField(max_length=100, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {} {}".format(self.id, self.date, self.first_name, self.last_name)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{} - {} @ {}".format(self.quantity, self.product.item_number, self.product.price)