from django.db import models

from django.contrib.auth.models import AbstractUser


class Admin(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('name', max_length=40, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField('password', max_length=255)


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField('name', max_length=40, unique=True)
    surname = models.CharField('name', max_length=120)
    password = models.CharField('password', max_length=255)


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('name', max_length=255)
    parent = models.CharField('parent', max_length=255)
    child = models.CharField('child', max_length=255)


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('name', max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField('price', default=10)
    count = models.IntegerField('count', default=0)
    rating = models.IntegerField('rating', default=5)


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)


class OrderedProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField('amount', default=1)
