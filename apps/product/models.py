# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify

from apps.brand.models import Brand
from apps.category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, blank=True,
                                 default=None)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
