from django.db import models
# from fcuser.models import Fcuser
# from fcproduct.models import Fcproduct
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name = "사용자")
    product_p = models.ForeignKey('product_p.Product_p',on_delete=models.CASCADE, verbose_name = "상품")
    quantity_p = models.IntegerField(verbose_name="수량")
    product_n = models.ForeignKey('product_n.Product_n',on_delete=models.CASCADE, verbose_name = "상품")
    quantity_n = models.IntegerField(verbose_name="수량")
    register_date = models.DateField()
    register_dttm = models.DateField(auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return str(self.user) + ' ' +str(self.register_dttm)


    class Meta:
        db_table = 'order'
        verbose_name = "주문"
        verbose_name_plural = "주문"