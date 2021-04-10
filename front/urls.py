from django.urls import path
from . import views


app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.ProductsDetail.as_view(), name='detail'),
]

