from django.contrib import admin
from .models import Product_n

# Register your models here.
class Product_NAdmin(admin.ModelAdmin):
    list_display = ('name','stock')

admin.site.register(Product_n,Product_NAdmin)