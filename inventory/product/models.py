from django.db import models

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name = "사용자")
    name_product = models.CharField(max_length=64,verbose_name="사용프린터")
    color_product = models.CharField(max_length=64,verbose_name="프린터색상")
    in_stock = models.IntegerField(verbose_name = "입고량")
    out_stock = models.IntegerField(verbose_name = "출고량")
    month_in = models.IntegerField(verbose_name = "해당월입고량")
    month_out = models.IntegerField(verbose_name = "해당월출고량")
    stock = models.IntegerField(verbose_name = "현재재고")
    description = models.TextField(verbose_name="내용")
    etc = models.TextField(verbose_name="비고")
    register_date = models.DateField()
    #register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return self.name_product
        
    class Meta:
        db_table = 'product'
        verbose_name = "상품"
        verbose_name_plural = "상품"