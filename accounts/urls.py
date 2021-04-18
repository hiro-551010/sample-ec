from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [  
    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', views.signup),
    path('mypage/', views.MypageView.as_view()),
]