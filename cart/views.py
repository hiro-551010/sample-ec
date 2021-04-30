from accounts.models import User, Profile
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem
from front.models import Product
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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
@login_required
def add_to_cart(request):
    cartitem = get_object_or_404(CartItem, slug=CartItem.slug)
    context = {
        'cartitem': cartitem,
    }
    return render(request, 'cart/cart_list.html', context)





class UpdateCartItem(UpdateView):
    model = CartItem
    template_name = 'cart/list_carts.html'

class DeleteCartItem(DeleteView):
    model = Cart
    template_name = 'cart/list_carts.html'