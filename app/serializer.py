
from app.models import Product
from rest_framework import serializers

# class ProductSerializer(serializers.Serializer):
#     name= serializers.CharField(max_length=30)
#     price= serializers.FloatField()
#     discount= serializers.FloatField()
#     duration= serializers.FloatField()
#     authodName= serializers.CharField(max_length=30)
    
#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)

#     def update(self, Plist, validated_data):
#         updateProduct= Product(**validated_data)
#         updateProduct.id = Plist.id
#         updateProduct.save()
#         return updateProduct

# code reusability
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        # fields=['name', 'price']    # specific fields
        fields='__all__'     # all fields