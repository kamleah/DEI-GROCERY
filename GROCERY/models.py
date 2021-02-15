from django.db import models

# Create your models here.
class Category(models.Model):
    category_id=models.IntegerField(primary_key=True)
    category_name=models.CharField(max_length=100)
    category_description=models.CharField(max_length=200)
    class Meta:
        db_table="category"

def upload_path(instance,filename):
    return '/'.join(['productImages',filename])

class Products(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=150)
    product_description=models.CharField(max_length=500)
    category_id=models.IntegerField()
    product_price=models.IntegerField()
    product_ImgUrl=models.ImageField(blank=True,null=True,upload_to=upload_path)
    class Meta:
        db_table="products"

class Users(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=50)
    user_role=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_phoneNo=models.IntegerField()
    user_address=models.TextField(max_length=250)
    class Meta:
        db_table="user"
    
class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    category_id = models.IntegerField()
    quantity = models.IntegerField()
    class Meta:
        db_table="cart"
    
# class Cart2(models.Model):
#     cart_id = models.IntegerField(primary_key=True)
#     user_id = models.IntegerField()
#     product_id = models.IntegerField()
#     category_id = models.IntegerField()
#     quantity = models.IntegerField()
#     class Meta:
#         db_table="cart2"

