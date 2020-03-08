from django.contrib import admin
from .models import Product_p

# Register your models here.
class Product_PAdmin(admin.ModelAdmin):
    list_display = ('name_printer','stock')

admin.site.register(Product_p,Product_PAdmin)