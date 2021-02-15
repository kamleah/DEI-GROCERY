from django.shortcuts import render
from GROCERY.models import Users,Category,Products,Cart
from GROCERY.serializers import UsersSerializers,CategorySerializers,ProductsSerializers,CartSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

#Category API Starts Here
#API created to get and post data in database of category
class CategoryView(APIView):
    def get(self,request,format=None):
        CategoryData=Category.objects.all()
        CategoryDataSerializers=CategorySerializers(CategoryData, many=True)
        return Response(CategoryDataSerializers.data)
    
    def post(self,request,format=None):
        InsertData = CategorySerializers(data=request.data)
        if InsertData.is_valid():
            InsertData.save()
            return Response(InsertData.data, status=status.HTTP_201_CREATED)
        return Response(InsertData.errors,status=status.HTTP_400_BAD_REQUEST)

#API created to get,put/patch or delete data from category database using category_id
class CategoryEdit(APIView):
    def get(self,request,id,format=None):
        CategoryData=Category.objects.get(category_id=id)
        CategoryDataSerializers=CategorySerializers(CategoryData)
        return Response(CategoryDataSerializers.data)

    def put(self, request, id, format=None):
        UpdateData = Category.objects.get(category_id=id)
        CategoryDataSerializers = CategorySerializers(UpdateData,data=request.data)
        if CategoryDataSerializers.is_valid():
            CategoryDataSerializers.save()
            return Response(CategoryDataSerializers.data)
        return Response(CategoryDataSerializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        deleteData = Category.objects.get(category_id=id)
        deleteData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Category API End's Here

#Product's API Start's Here
#API created to get and post data in database of Products
class ProductsView(APIView):
    def get(self,request,format=None):
        ProductsData=Products.objects.all()
        ProductsDataSerializers=ProductsSerializers(ProductsData, many=True)
        return Response(ProductsDataSerializers.data)
    
    def post(self,request,format=None):
        InsertData = ProductsSerializers(data=request.data)
        if InsertData.is_valid():
            InsertData.save()
            return Response(InsertData.data, status=status.HTTP_201_CREATED)
        return Response(InsertData.errors,status=status.HTTP_400_BAD_REQUEST)

#API created to get,put/patch or delete data from Products database using category_id
class ProductsEdit(APIView):
    def get(self,request,id,format=None):
        ProductsData=Products.objects.get(product_id=id)
        ProductsDataSerializers=ProductsSerializers(ProductsData)
        return Response(ProductsDataSerializers.data)

    def put(self, request, id, format=None):
        UpdateData = Products.objects.get(category_id=id)
        ProductsDataSerializers = ProductsSerializers(UpdateData,data=request.data)
        if ProductsDataSerializers.is_valid():
            ProductsDataSerializers.save()
            return Response(ProductsDataSerializers.data)
        return Response(ProductsDataSerializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        deleteData = Products.objects.get(product_id=id)
        deleteData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Product's API End's Here

#User API Starts From Here
#API created to get and post data in database of user
class UserView(APIView):
    def get(self,request,format=None):
        userData=Users.objects.all()
        UsersDataSerializers=UsersSerializers(userData, many=True)
        return Response(UsersDataSerializers.data)
    
    def post(self,request,format=None):
        InsertData = UsersSerializers(data=request.data)
        if InsertData.is_valid():
            InsertData.save()
            return Response(InsertData.data, status=status.HTTP_201_CREATED)
        return Response(InsertData.errors,status=status.HTTP_400_BAD_REQUEST)

#API created to get,put/patch or delete data from user database using user_id
class UserEdit(APIView):
    def get(self,request,id,format=None):
        userData=Users.objects.get(user_id=id)
        UsersDataSerializers=UsersSerializers(userData)
        return Response(UsersDataSerializers.data)

    def put(self, request, id, format=None):
        UpdateData = Users.objects.get(user_id=id)
        UsersDataSerializers = UsersSerializers(UpdateData,data=request.data)
        if UsersDataSerializers.is_valid():
            UsersDataSerializers.save()
            return Response(UsersDataSerializers.data)
        return Response(UsersDataSerializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        deleteData = Users.objects.get(user_id=id)
        deleteData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#User API End's Here

#Cart API Start's Here
#API created to get and post data in database of Cart
class CartView(APIView):
    def get(self,request,format=None):
        CartData=Cart.objects.all()
        CartDataSerializers=CartSerializers(CartData, many=True)
        return Response(CartDataSerializers.data)
    
    def post(self,request,format=None):
        InsertData = CartSerializers(data=request.data)
        if InsertData.is_valid():
            InsertData.save()
            return Response(InsertData.data, status=status.HTTP_201_CREATED)
        return Response(InsertData.errors,status=status.HTTP_400_BAD_REQUEST)

#API created to get,put/patch or delete data from user database using user_id
class CartEdit(APIView):
    def get(self,request,id,format=None):
        CartData=Cart.objects.get(cart_id=id)
        CartDataSerializers=CartSerializers(CartData)
        return Response(CartDataSerializers.data)

    def put(self, request, id, format=None):
        UpdateData = Cart.objects.get(cart_id=id)
        CartDataSerializers = CartSerializers(UpdateData,data=request.data)
        if CartDataSerializers.is_valid():
            CartDataSerializers.save()
            return Response(CartDataSerializers.data)
        return Response(CartDataSerializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        deleteData = Cart.objects.get(cart_id=id)
        deleteData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Cart API END's Here
