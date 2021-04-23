from accounts.models import User
from django.db.models.fields import proxy
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem
from accounts.models import Profile

##-------------- Cart Views --------------------------------------
class ListCart(ListView):
    model = Cart
    context_object_name = 'carts'
    template_name = 'cart/cart.html'

    #cartのhtmlにusernameを表示させるための関数
    def get_context_data(self, **kwargs):
        profile = super().get_context_data(**kwargs)
        profile['username'] = Profile.objects.filter(user=self.request.user).first().username
        cart_id = super().get_context_data(**kwargs)
        cart_id['cart_id'] = User.objects.filter(user=self.request.user).first().Caer
        return profile, cart_id


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