from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import DJuser
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def home(request):
    user_id = request.session.get('user')
    if user_id:
        djuser = DJuser.objects.get(pk=user_id)
        return HttpResponse(djuser.username)
    return HttpResponse("Home!")


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else:
            try:
                djuser = DJuser.objects.get(username=username)
            except(DJuser.DoesNotExist):
                res_data['error'] = '아이디가 틀렸습니다.'
                return render(request, "login.html", res_data)
            if check_password(password, djuser.password):
                request.session['user'] = djuser.id
                return redirect('/')
            else:
                res_data['error'] = '비밀번호를 틀렸습니다.'

        return render(request, "login.html", res_data)


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
