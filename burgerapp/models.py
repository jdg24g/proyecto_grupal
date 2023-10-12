from django.db import models

# Create your models here.

# Create User model using django ORM
class User(models.Model):

    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)
    email_address   = models.CharField(max_length=255)
    password        = models.CharField(max_length=255)
    phone_number    = models.CharField(max_length=255, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email_address} {self.phone_number} {self.created_at} {self.updated_at}"