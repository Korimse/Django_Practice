from django.shortcuts import render
from .models import DJuser
from django.contrib.auth.hashers import make_password

# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if not (username and email and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            djuser = DJuser(
                username=username,
                useremail=email,
                password=make_password(password),
            )
            djuser.save()
        return render(request, "register.html", res_data)
