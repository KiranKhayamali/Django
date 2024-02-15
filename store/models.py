from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default='', blank=True)
    sku = models.CharField(verbose_name="Stock Keeping Unit", max_length=20, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['price']
        constraints = [
            models.CheckConstraint(check=models.Q(price__gte=0), name="price_not_negative")
        ]

    def get_absolute_url(self):
        # return reverse("store:product-detail", kwargs={'pk': self.id})
        return reverse("store")

    @property
    def vat(self):
        return Decimal(.2) * self.price

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Product')

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name