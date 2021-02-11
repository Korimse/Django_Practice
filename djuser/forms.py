from django import forms
from .models import DJuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': '아이디를 입력해주세요'}, max_length=32, label="사용자 이름")
    password = forms.CharField(error_messages={
                               'required': '비밀번호를 입력해주세요'}, widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                djuser = DJuser.objects.get(username=username)
                if not check_password(password, djuser.password):
                    self.add_error('password', '비밀번호가 틀렸습니다.')
                else:
                    self.user_id = djuser.id
            except(DJuser.DoesNotExist):
                self.add_error('username', '아이디가 존재하지 않습니다.')
