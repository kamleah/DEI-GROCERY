"""DEIBACKEND URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from GROCERY.views import Users
from GROCERY import views
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/',views.CategoryView.as_view()),
    path('category/<int:id>',views.CategoryEdit.as_view()),
    path('product/',views.ProductsView.as_view()),
    path('product/<int:id>',views.ProductsEdit.as_view()),
    path('addUser/',views.UserView.as_view()),
    path('editUser/<int:id>',views.UserEdit.as_view()),
    path('cart/',views.CartView.as_view()),
    path('editcart/<int:id>',views.CartEdit.as_view())
]
