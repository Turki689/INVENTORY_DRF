from django.contrib import admin

from apps.category.models import Category
from apps.product.models import Product, Brand
from apps.product_line.models import ProductLine


class Productlineinline(admin.TabularInline):
    model = ProductLine


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [Productlineinline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class CategoryAdmin(admin.ModelAdmin):
    pass

# Register your models here.
