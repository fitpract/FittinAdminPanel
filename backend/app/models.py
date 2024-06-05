from django.db import models

from django.contrib.auth.models import AbstractUser


class Admin(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('name', max_length=40, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField('password', max_length=255)


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('name', max_length=40, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField('password', max_length=255)
    confirmed = models.BooleanField(default=False, verbose_name="confirmed")


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('name', max_length=255)
    parent = models.CharField('parent', max_length=255)
    child = models.CharField('child', max_length=255)


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('name', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField('price', default=10)
    count = models.IntegerField('count', default=0)
    rating = models.IntegerField('rating', default=5)


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
