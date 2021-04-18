from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from accounts.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm

class Login(LoginView):
    template_name = 'accounts/auth.html'

    def form_valid(self, form):
        messages.success(self.request,'ログイン完了しました')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'エラーがありました')
        return super().form_invalid(form)

def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            #userのメソッドを使いたいけど、セーブは待って欲しい時に使う
            user = form.save(commit=False)

            #メール認証してからuser.saveする場合はこれを使う
            #user.is_active = False

            user.save()

            #ログインさせる
            login(request, user)

            messages.success(request,'登録完了しました')
            return redirect('/')
    return render(request, 'accounts/auth.html', context)

class MypageView(LoginRequiredMixin, View):
    context = {}

    def get(self, request):
        return render(request, 'accounts/mypage.html', self.context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,'更新完了しました')
        return render(request, 'accounts/mypage.html', self.context)