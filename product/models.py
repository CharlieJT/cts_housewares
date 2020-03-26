from django.db import models

# Create your models here.
class Product(models.Model):
    item_number = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    brand = models.CharField(max_length=100)
    about_product = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    stock = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.item_number


class Image(models.Model):
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.product.item_number


class Specification(models.Model):
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    specification = models.CharField(max_length=250)

    def __str__(self):
        return self.product.item_number