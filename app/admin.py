from django.contrib import admin
from app.models import Product
# Register your models here.
class ProductViews(admin.ModelAdmin):
    list_diaplay=['name','price', 'discount']

admin.site.register(Product, ProductViews)
