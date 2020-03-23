from django.contrib import admin
from .models import Product, Image

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )


admin.site.register(Product, ProductAdmin)