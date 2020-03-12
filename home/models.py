from django.db import models

# Create your models here.
class Banner(models.Model):
    brand = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    mobile_image = models.ImageField(upload_to='images')
    tablet_image = models.ImageField(upload_to='images')
    desktop_image = models.ImageField(upload_to='images')

    def __str__(self):
        return  self.brand
