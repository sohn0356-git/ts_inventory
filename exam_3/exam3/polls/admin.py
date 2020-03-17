from django.contrib import admin
from .models import Question, Choice, Product_p, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_printer','color_printer','name_toner','color_toner','stock','register_date')      #field들이 listing됨

class Product2Admin(admin.ModelAdmin):
    list_display = ('name_product','color_product','stock','register_date')      #field들이 listing됨

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Product_p, ProductAdmin)
admin.site.register(Product, Product2Admin)