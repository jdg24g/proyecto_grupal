from django.contrib import admin
from burgerapp import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Products)
admin.site.register(models.Cities)
admin.site.register(models.Sucursal)
admin.site.register(models.Stock)