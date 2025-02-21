from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, related_name='children', null=True, blank=True, )
    slug = models.SlugField(max_length=255,unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


# Create your models here.
