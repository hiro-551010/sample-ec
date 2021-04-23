from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from accounts.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm

from cart.models import Cart

class Login(LoginView):
    template_name = 'accounts/auth.html'

    def form_valid(self, form):
        messages.success(self.request,'ログイン完了しました')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'エラーがありました')
        return super().form_invalid(form)

def signup(request):
    form = UserCreationForm(request.POST)
    context = {
        'form': form
    }
    if request.method == 'POST':
        
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            """
            cart = Cart.objects.create(user=user)
            cart = form.save(commit=False)
            cart.save()
            """
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