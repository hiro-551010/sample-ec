from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('list/<int:pk>', views.ListCart.as_view(), name='list'),
]

# CartItem Urls
urlpatterns += [
    path('cartitem/create/', views.CreateCartItem.as_view(), name='create-cartitem'),
    path('cartitem/<int:pk>/update/', views.UpdateCartItem.as_view(), name='update-cartitem'),
    path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(), name='delete-cartitem'),
]
