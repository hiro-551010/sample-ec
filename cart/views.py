
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem

##-------------- Cart Views --------------------------------------

class DetailCart(DetailView):
    model = Cart
    template_name = 'cart/detail_cart.html'

class ListCart(ListView):
    model = Cart
    context_object_name = 'carts'
    template_name = 'cart/list_carts.html'

class CreateCart(CreateView):
    model = Cart
    template_name = 'cart/list_carts.html'

class Updatecart(UpdateView):
    model = Cart
    template_name = 'cart/list_carts.html'

class DeleteCart(DeleteView):
    model = Cart
    template_name = 'cart/list_carts.html'


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