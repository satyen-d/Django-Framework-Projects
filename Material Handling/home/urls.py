from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth.views import LoginView, LogoutView


from home.views import user_login, success, user_logout 



urlpatterns = [
    path('', views.authen),
    path('logout/authen/', views.authen),
    path('index/pay', views.Pay),
    path('contactus', views.contactus),
    path('transport', views.Transports),
    path('index/material', views.materials),
    path('shoperg', views.shoperg),
    path('transrg', views.transrg),
    path('login/', LoginView.as_view(), name="login_url"),
    path('logout/', LogoutView.as_view(next_page = 'authen/'), name="logout"),
    path('register/', views.registerview, name="register_url"),
    path('index/Shopreg/', views.shopregistration, name="shopreg"),
    path('index/', views.index, name="index"),
    path('Order', views.order, name="index"),
    path('rohatrans', views.Rohatrans, name="index"),
    path('punetrans', views.Punetrans, name="index"),
    path('mumbaitrans', views.Mumbaitrans, name="index"),
    path('index/pune', views.Pune, name="index"),
    path('index/roha', views.Roha, name="index"),
    path('index/mumbai', views.Mumbai, name="index"),
    path('index/Transreg/', views.transregistration, name="transreg"),
    path('index/contactus/', views.contactus, name="contactus"),

]
