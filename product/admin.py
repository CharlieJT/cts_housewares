from django.contrib import admin
from .models import Product, Image, Specification

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image

class SpecificationInline(admin.TabularInline):
    model = Specification

class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageInline, SpecificationInline, )


admin.site.register(Product, ProductAdmin)