from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Product, OrderHistory
from cart.models import CartItem, Cart
from accounts.models import  User
from django.utils import timezone


# --- stripe決済 ---
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRETS_KEY
# --- stripe決済 ---


def index(request):
    product = Product.objects.all()
    context = {
        'product': product,
    }
    return render(request, 'front/index.html', context)


class ProductsDetail(DetailView):
    model = Product
    template_name = 'front/detail.html'

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
            return render(request, 'cart:list', context)
        else:
            OrderHistory.objects.create(product=product, email=request.user, price=product.price, stripe_id=charge.id, order_at=timezone.now)
            return redirect('cart:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['public_key'] = settings.STRIPE_PUBLIC_KEY
        context['is_added'] = CartItem.objects.filter(cart_id=self.request.user.pk,product_id=kwargs.get('object').id).first()
        return context
    # --- stripe決済 ---


def historys(request):
    historys = OrderHistory.objects.all()
    context = {
        'historys': historys,
    }
    print(context["historys"])
    return render(request, 'front/historys.html', context)




    