from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email_address} {self.phone_number} {self.created_at} {self.updated_at}"


class Products(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.product_name} {self.price} {self.description}"


class Cities(models.Model):
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city_name}"


class Sucursal(models.Model):
    nombre = models.CharField(max_length=255)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.city}"


class Stock(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.products} {self.sucursal} {self.quantity}"
