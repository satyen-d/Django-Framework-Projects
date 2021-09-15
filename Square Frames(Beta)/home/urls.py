from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('aboutus', views.aboutus),
    path('contactus', views.contactus),
    path('index', views.index),
    path('testimonials', views.testimonials),
    path('bird', views.bird),
    path('landscape', views.landscape),
    path('still', views.still),
    path('mission', views.mission),
    path('buybird', views.buybird),
    path('order', views.order),
    path('portfolio', views.portfolio),
    path('specials', views.specials),
    path('upload', views.upload)

]
