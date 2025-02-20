from django.contrib import admin

from apps.product_line.models import ProductLine


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    pass
