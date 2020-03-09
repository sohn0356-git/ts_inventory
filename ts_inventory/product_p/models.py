from django.db import models

# Create your models here.
class Product_p(models.Model):
    name_printer = models.CharField(max_length=64,verbose_name="사용프린터")
    name_toner = models.CharField(max_length=64,verbose_name="토너명")
    category_toner = models.CharField(max_length=64,verbose_name="토너종류")
    pre_stock = models.IntegerField(verbose_name="전월재고")
    in_stock = models.IntegerField(verbose_name="입고수량")
    out_stock = models.IntegerField(verbose_name="출고수량")
    out_description = models.CharField(max_length=64,verbose_name="출고내역")
    stock = models.IntegerField(verbose_name = "현재재고")
    remark = models.CharField(max_length=64,verbose_name="비고")
    register_date_start = models.DateField()
    register_date_end = models.DateField()
    #register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return self.name_printer
        
    class Meta:
        db_table = 'product_p'
        verbose_name = "상품"
        verbose_name_plural = "상품"