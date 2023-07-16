from django.contrib import admin

from applications.product.models import Product, Image

admin.site.register(Product)
admin.site.register(Image)