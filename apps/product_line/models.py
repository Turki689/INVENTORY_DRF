from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify

from apps.product.models import Product


class ProductLine(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)]
                                )
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    sku = models.CharField(max_length=120)
    is_active = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_lines')
    slug = models.SlugField(max_length=120, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
# Create your models here.
