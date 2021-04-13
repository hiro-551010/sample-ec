from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.ProductsDetail.as_view(), name='detail'),
    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', views.signup),

]

