from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('list/', views.CartItemView.as_view(), name='list'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:pk>', views.CartUpdateView.as_view(), name='update'),
    path('delete_cart/<int:pk>', views.CartDeleteView.as_view(), name='delete'),
]

