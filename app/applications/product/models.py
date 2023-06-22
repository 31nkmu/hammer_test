from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='electronics')

    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    short_description = models.TextField(null=True, blank=True)
    full_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
