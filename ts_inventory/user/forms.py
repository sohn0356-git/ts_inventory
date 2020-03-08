from django import forms
from .models import User
from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(forms.Form):
    userid = forms.CharField(
        error_messages={
            'required' : '아이디을 입력해주세요'
        }, max_length = 64, label='아이디'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', "비밀번호가 서로 다릅니다")
                self.add_error('re_password', "비밀번호가 서로 다릅니다")
            

class LoginForm(forms.Form):
    userid = forms.CharField(
        error_messages={
            'required' : '아이디을 입력해주세요'
        }, max_length = 64, label='아이디'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')

        if userid and password:
            try:
                user = User.objects.get(userid=userid)
            except User.DoesNotExist:
                self.add_error('userid', "해당 아이디가 없습니다")
                return
            if not check_password(password, user.password):
                self.add_error('password', "비밀번호가 틀렸습니다")