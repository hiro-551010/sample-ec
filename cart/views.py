from accounts.models import User, Profile
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem
from front.models import Product
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404, response
##-------------- Cart Views --------------------------------------
class ListCart(ListView):
    model = Cart
    template_name = 'cart/cart_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = Profile.objects.filter(user=self.request.user).first().username
        context['cart'] = Cart.objects.filter(cart=self.request.user).first()
        return context

##-------------- CartItem Views --------------------------------------
@login_required
def add_to_cart(request):
    if request.is_ajax:
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        product = get_object_or_404(Product,id=product_id)
        if int(quantity) <= 0:
            response = JsonResponse({'message': '０より大きい数字を入れてください'})
            response.status_code = 403
            return response
        cart = Cart.objects.get_or_create(cart=request.user)
        if all([product_id, cart, quantity]):
            CartItem.objects.save_item(quantity=quantity, product_id=product_id,cart=cart[0])
            return JsonResponse({'message': '商品をカートに入れました'})



    return redirect('cart/cart_list.html')






