from accounts.models import User, Profile
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem

##-------------- Cart Views --------------------------------------
class ListCart(ListView):
    model = Cart
    #context_object_name = 'cart'
    template_name = 'cart/cart_list.html'

    #cartのhtmlにusernameを表示させるための関数
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = Profile.objects.filter(user=self.request.user).first().username
        context['cart'] = Cart.objects.filter(cart_id=self.request.user.pk).first()
        return context



##-------------- CartItem Views --------------------------------------
class DetailCartItem(DetailView):
    model = CartItem
    template_name = 'cart/detail_cart.html'

class ListCartItem(ListView):
    model = CartItem
    context_object_name = 'cartitems'
    template_name = 'cart/list_carts.html'

class CreateCartItem(CreateView):
    model = CartItem
    template_name = 'cart/list_carts.html'

class UpdateCartItem(UpdateView):
    model = CartItem
    template_name = 'cart/list_carts.html'

class DeleteCartItem(DeleteView):
    model = Cart
    template_name = 'cart/list_carts.html'