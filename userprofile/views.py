from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegisterForm

from .forms import ProfileForm
from .models import Profile


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data
            data = user_login_form.cleaned_data
            # user 
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                #session 
                login(request, user)
                return redirect("article:article_list")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = { 'form': user_login_form }
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")



def user_logout(request):
    logout(request)
    return redirect("index")


def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            login(request, new_user)
            return redirect("article:article_list")
        else:
            return HttpResponse("注册表单输入有误。请再次检查输入密码是否符合标准，并重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


@login_required(login_url='/userprofile/login/')
def user_delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        # 验证登录用户、待删除用户是否相同
        if request.user == user:
            #退出登录，删除数据并返回博客列表
            logout(request)
            user.delete()
            return redirect("article:article_list")
        else:
            return HttpResponse("你没有删除操作的权限。")
    else:
        return HttpResponse("仅接受post请求。")

@login_required(login_url='/userprofile/login/')
def profile_edit(request, id):
    user = User.objects.get(id=id)

    # profile = Profile.objects.get(user_id=id)
    # Profile
    if Profile.objects.filter(user_id=id).exists():
        # user_id OneToOneField
        profile = Profile.objects.get(user_id=id)
    else:
        profile = Profile.objects.create(user=user)


    if request.method == 'POST':
        if request.user != user:
            return HttpResponse("你没有权限修改此用户信息。")

        # request.FILES 
        profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data

            profile.phone = profile_cd['phone']
            profile.bio = profile_cd['bio']

            #request.FILES 
            if 'avatar' in request.FILES:
                profile.avatar = profile_cd["avatar"]

            profile.save()
            #redirect()
            return redirect("userprofile:edit", id=id)
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")

    elif request.method == 'GET':
        profile_form = ProfileForm()
        context = { 'profile_form': profile_form, 'profile': profile, 'user': user }
        return render(request, 'userprofile/edit.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")
