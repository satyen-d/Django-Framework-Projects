from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('contactus', views.contactus),
    path('aboutus', views.aboutus),
    path('ladies', views.ladies),
    path('electrical', views.electrical),
    path('other', views.other),

]
 