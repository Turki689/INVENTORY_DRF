# Generated by Django 5.1.6 on 2025-02-24 14:31

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('stock_quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('sku', models.CharField(max_length=120)),
                ('is_active', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=120, null=True, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_lines', to='product.product')),
            ],
        ),
    ]
