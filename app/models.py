
from django.db import models
from rest_framework import serializers

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=30)
    price= models.FloatField()
    discount= models.FloatField()
    duration= models.FloatField()
    authodName= models.CharField(max_length=30)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= '__all__'
