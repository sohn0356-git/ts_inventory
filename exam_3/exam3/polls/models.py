from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model): # 항상 Model 클래스를 상속받는다
    #pk 는 자동으로 생성
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 날짜가 최근 24시간 이내 작성된거라면 True를 리턴한다.
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # 질문을 삭제 했을 때 연관 항목을 어떻게 할지 설정 - 자동 삭제
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 128)
    votes = models.IntegerField(default = 0)
    category = models.CharField(max_length=128)
    def __str__(self):
        return self.choice_text


class Product_p(models.Model):
    name_printer = models.CharField(max_length=64,verbose_name="사용프린터")
    color_printer = models.CharField(max_length=64,verbose_name="프린터색상")
    name_toner = models.CharField(max_length=64,verbose_name="토너명")
    color_toner = models.CharField(max_length=64,verbose_name="토너색상")
    category_toner = models.CharField(max_length=64,verbose_name="토너종류")
    stock = models.IntegerField(verbose_name = "현재재고")
    register_date = models.DateField()
    #register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return self.name_printer
        
    class Meta:
        db_table = 'product_p'
        verbose_name = "상품"
        verbose_name_plural = "상품"