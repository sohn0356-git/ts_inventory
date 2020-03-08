from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','register_dttm')

admin.site.register(Order,OrderAdmin)