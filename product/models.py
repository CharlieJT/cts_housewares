from django.db import models

# Create your models here.
class Product(models.Model):
    item_number = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    about_product = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    image = models.ImageField(upload_to='images')
    stock = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.item_number