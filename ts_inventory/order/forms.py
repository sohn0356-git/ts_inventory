from django import forms
from .models import Order
from product_p.models import Product_p
from user.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.db import transaction

class RegisterForm_P(forms.Form):

    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required' : '수량을 입력해주세요'
        }, label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required' : '상품을 입력해주세요'
        }, label='상품', widget = forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')

        print(self.request.session)
        user = self.request.session.get('user')
        if quantity and product and user:
            prod = product.objects.get(pk=product)
            if not (prod.stock >= quantity and quantity > 0):
                self.add_error('quantity', '재고보다 많은 양을 입력하였습니다') 
        else:
            self.product = product
            self.add_error('quantity', '값이 없습니다')
            self.add_error('product', '값이 없습니다')
        
