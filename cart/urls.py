from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('list/<int:pk>', views.ListCart.as_view(), name='list'),
]

# CartItem Urls
urlpatterns += [
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cartitem/<int:pk>/update/', views.UpdateCartItem.as_view(), name='update-cartitem'),
    path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(), name='delete-cartitem'),
]
