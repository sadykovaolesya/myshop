from django.db import models

class ProdactCategiry(models.Model):
    name = models.CharField(verbose_name="name", max_length=64, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProdactCategiry, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="name_product", max_length=128)
    image = models.ImageField(upload_to = "product_images", blank=True)
    description = models.TextField(verbose_name="description", blank=True)
    price = models.DecimalField(verbose_name="price", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="quantity in store", default=0)

    def __str__(self):
        return f"{self.name}({self.category})"
# Create your models here.
