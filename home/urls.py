from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

path('', views.home, name='home'),
path('about', views.about, name='about'),
path('contact', views.contact, name='contact'),
path('signup', views.handlesignup, name='handlesignup'),
path('login', views.handlelogin, name='handlelogin'),
path('logout', views.handlelogout, name='handlelogout'),
]