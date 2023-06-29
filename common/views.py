from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import  get_user_model
from allauth.account.views import SignupView
from django.contrib.auth import login

# 회원 가입

def detail(request, id):
    user = get_user_model()
    user = get_object_or_404(user, id=id)
    context = {
        'user': user
    }

    return render(request, 'common/detail.html', context)



class CustomSignupView(SignupView):
    def form_valid(self, form):
        # 회원가입 폼이 유효할 경우 회원가입 처리
        response = super().form_valid(form)
        # 회원가입한 사용자를 자동으로 로그인 처리
        login(self.request, self.user)
        return response