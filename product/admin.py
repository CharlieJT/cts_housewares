from django.contrib import admin
from .models import Product, Image, Specification, Dimension

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image

class SpecificationInline(admin.TabularInline):
    model = Specification

class DimensionInline(admin.TabularInline):
    model = Dimension

class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageInline, SpecificationInline, DimensionInline, )


admin.site.register(Product, ProductAdmin)