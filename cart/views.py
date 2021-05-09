from accounts.models import User, Profile
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView,TemplateView
from .models import Cart, CartItem
from front.models import Product
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404, response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CartUpdateForm
from front.models import OrderHistory
from django.conf import settings

# --- stripe決済 ---
import stripe
from django.utils import timezone
stripe.api_key = settings.STRIPE_SECRETS_KEY
# --- stripe決済 ---

##-------------- Cart Views --------------------------------------
"""
class ListCart(ListView):
    model = Cart
    template_name = 'cart/cart_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.user.pk
        return context
"""

class CartItemView(LoginRequiredMixin, TemplateView):
    template_name = 'cart/cart_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.pk
        profile = Profile.objects.all()
        query = CartItem.objects.filter(cart_id=user_id)
        total_price = 0
        items = []
        for item in query.all():
            total_price += item.quantity * item.product.price
            picture = item.product.image
            tmp_item = {
                'quantity': item.quantity,
                'picture': picture,
                'name': item.product.name,
                'id': item.id,
                'price': item.product.price,
            }
            items.append(tmp_item)
        context['total_price'] = total_price
        context['items'] = items
        context['public_key'] = settings.STRIPE_PUBLIC_KEY
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        address = context.get('address')
        total_price = context.get('total_price')
        product = context.get('items') 
        #cart = context['cart']
        token = request.POST('stripeToken')
        if (not address):
            raise Http404('注文処理でエラーが発生しました')
        try:
            charge = stripe.Charge.create(
                amount=total_price,
                currency='jpy',
                source=token,
            )
        except stripe.error.CartError as e:
            raise Http404('注文処理でエラーが発生しました')
        else:
            OrderHistory.objects.create(user=request.user, product=product, quantity=item.quantity, price=product.price, stripe_id=charge.id, order_at=timezone.now)
            return render(request, 'cart:list', context)

##-------------- CartItem Views --------------------------------------
@login_required
def add_to_cart(request):
    if request.is_ajax:
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        product = get_object_or_404(Product, id=product_id)
        if int(quantity) <= 0:
            response = JsonResponse({'message': '０より大きい数字を入れてください'})
            response.status_code = 403
            return response
        cart = Cart.objects.get_or_create(cart=request.user)
        if all([product_id, cart, quantity]):
            CartItem.objects.save_item(quantity=quantity, product_id=product_id,cart=cart[0])
            return JsonResponse({'message': '商品をカートに入れました'})
    return redirect('cart/cart_list.html')

class CartUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'cart/update_cart.html'
    form_class = CartUpdateForm
    model = CartItem
    success_url = reverse_lazy('cart:list')

class CartDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'cart/delete_cart.html'
    model = CartItem
    success_url = reverse_lazy('cart:list')



    




