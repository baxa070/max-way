from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    combo = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=False)
    price = models.PositiveIntegerField(blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    foods = models.ManyToManyField('self', blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    products = models.JSONField(blank=False, null=False)
    total_price = models.PositiveIntegerField(default=0)
    status = models.IntegerField(blank=False, null=False, default=1)
    created_at = models.DateField(auto_now_add=True)


class Delilveryinfo(models.Model):
    order = models.ForeignKey(Order, blank=False, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=False, default=0)
    payment_type = models.IntegerField(blank=False, null=False, default=0)
    address = models.TextField()
    created_at = models.DateField(auto_now_add=True)