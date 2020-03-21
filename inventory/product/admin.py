from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product','color_product','stock','register_date','user')      #field들이 listing됨

admin.site.register(Product, ProductAdmin)