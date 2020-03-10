from django import forms
from .models import Product_p

from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(forms.Form):
    name_printer = forms.CharField(
        error_messages={
            'required' : '사용프린터를 입력해주세요'
        }, max_length = 64, label='사용프린터'
    )
    name_toner = forms.CharField(
        error_messages={
            'required' : '토너명을 입력해주세요'
        }, max_length = 64, label='토너명'
    )
    category_toner = forms.CharField(
        error_messages={
            'required' : '토너종류를 입력해주세요'
        }, max_length = 64, label='토너종류'
    )
    pre_stock = forms.IntegerField(
        required=False, label='전월재고'
    )
    in_stock = forms.IntegerField(
        required=False, label='입고수량'
    )
    out_stock = forms.IntegerField(
        required=False, label='출고수량'
    )
    out_description = forms.CharField(
        required=False, max_length = 64, label='출고내역'
    )
    stock = forms.IntegerField(
        error_messages={
            'required' : '재고를 입력해주세요'
        }, label='재고'
    )
    remark = forms.CharField(
        required=False, max_length = 64, label='비고'
    )
    register_date_start = forms.DateField(
        error_messages={
            'required' : '입고날짜의 시작을 입력해주세요'
        },  widget=forms.DateInput(format='%m/%d/%Y') ,label='입고날짜'
    )
    register_date_end = forms.DateField(
        required=False,  widget=forms.DateInput(format='%m/%d/%Y') ,label='입고날짜'
    )
    def clean(self):
        cleaned_data = super().clean()
        name_printer= cleaned_data.get('name_printer')
        name_toner= cleaned_data.get('name_toner')
        category_toner = cleaned_data.get('category_toner')
        pre_stock = cleaned_data.get('pre_stock')
        in_stock = cleaned_data.get('in_stock')
        out_stock = cleaned_data.get('out_stock')
        out_description = cleaned_data.get('out_description')
        stock = cleaned_data.get('stock')
        remark = cleaned_data.get('remark')
        register_date_start= cleaned_data.get('register_date_start')
        register_date_end= cleaned_data.get('register_date_end')

class SearchForm(forms.Form):
    register_date_start = forms.DateField(
        error_messages={
            'required' : '날짜의 시작을 입력해주세요'
        },  widget=forms.DateInput(format='%m/%d/%Y') ,label='시작날짜 : '
    )
    register_date_end = forms.DateField(
        error_messages={
            'required' : '날짜의 끝을 입력해주세요'
        },  widget=forms.DateInput(format='%m/%d/%Y') ,label='끝 날짜 : '
    )

    def clean(self):
        cleaned_data = super().clean()
        register_date_start= cleaned_data.get('register_date_start')
        register_date_end= cleaned_data.get('register_date_end')
