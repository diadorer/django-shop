from django.db import models


class Product(models.Model):
    """Товар магазина."""
    name = models.CharField(max_length=250)
    price = models.FloatField()
    quantity = models.IntegerField()
    vender_code = models.CharField(max_length=50)
    # Поле со стоимостью товара



# Create your models here.
