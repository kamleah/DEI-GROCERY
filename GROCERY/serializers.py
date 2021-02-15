from rest_framework import serializers
from GROCERY.models import Products,Category,Users,Cart

# Category serializers
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'

# Product serializers
class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields="__all__"

# Users serializers
class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields = '__all__'
    
# Users serializers
class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"