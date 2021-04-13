from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View, DetailView
from .models import Product
from django.contrib.auth.views import LoginView
from django.contrib import messages
from front.forms import UserCreationForm
from django.contrib.auth import login
"""
# --- stripe決済 ---
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_PUBLIC_KEY
# --- stripe決済 ---
"""

def index(request):
    product = Product.objects.all()
    context = {
        'product': product,
    }
    return render(request, 'front/index.html', context)


class ProductsDetail(DetailView):
    template_name = 'front/detail.html'
    model = Product

        
"""
    # --- stripe決済 ---
    def post(self, request, *args, **kwargs):
        product = self.get_object()
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(
                amount=product.price, 
                currency='jpy', 
                source=token,
                )
        except stripe.error.CardError as e:
            context = self.get_context_data()
            context['message'] = 'カード決済に失敗しました'
            return render(request, self.template_name, context)
        else:
            return redirect('front:detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['public_key'] = settings.STRIPE_PUBLIC_KEY
        return context
    # --- stripe決済 ---
"""



class Login(LoginView):
    template_name = 'front/auth.html'

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
    return render(request, 'front/auth.html', context)



    