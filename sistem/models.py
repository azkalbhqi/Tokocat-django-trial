from django.db import models


class Paint(models.Model):
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand_name = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.brand_name} - {self.color} - Stock: {self.stock}"