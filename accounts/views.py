from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from accounts.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from cart.models import Cart
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Profile

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
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid():
            user = form_user.save(commit=False)
            user.save()
            cart = Cart.objects.create(cart=user)
            cart.save()
            login(request, user)
            messages.success(request,'登録完了しました')
            return redirect('/')
    return render(request, 'accounts/auth.html', context)

class MypageView(LoginRequiredMixin, View):
    template_view = 'accounts/mypage.html'
    success_url = reverse_lazy('cart:list')
    def get(self, request):
        return render(request, 'accounts/mypage.html')

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,'更新完了しました')
        return render(request, 'accounts/mypage.html')