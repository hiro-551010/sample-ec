from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Product
from cart.models import CartItem, Cart
from accounts.models import User

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
    model = Product
    template_name = 'front/detail.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['is_added'] = CartItem.objects.filter(cart_id=self.request.user.pk,product_id=kwargs.get('object').id).first()
        """
        #①
        context['product_id'] = CartItem.objects.filter(product_id=kwargs.get('object').id).first()
        #②
        print(self.request.user.pk)
        #③
        context['cartitem'] = CartItem.objects.filter().first()

        #④
        print(context['product_id'])

        print(context['cartitem'])
        """
        return context
        
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







    