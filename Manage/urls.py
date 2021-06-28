from django.contrib import admin
from django.urls import path, include
from . import views

#Admin Login 
admin.site.site_header = "Home-Foods Admin"
admin.site.site_title = "Home-Foods Admin"
admin.site.index_title = "Welcome to Home-Foods Admin Panel"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signup/', views.handleSignup, name='handleSignup'),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),
    path('forgotpass/', views.handleforgotpass, name='handleforgotpass'),
    path('custdets/', views.handlecustdets, name='handlecustdets'),
    path('editprofile/', views.handleeditprofile, name='handleeditprofile'),
    path('orderdets/', views.handleorderdets, name='handleorderdets'),
    path('userdets/', views.handleuserdets, name='handleuserdets'),
     path('additem/', views.handleadditem, name='handleadditem'),
    path('additem/<int:itemid>/modify/', views.handlemodify, name='handlemodify'),
    path('additem/<int:itemid>/modify/updated/', views.handlemodified, name='handlemodified'),
    path('additem/<int:itemid>/delete/',views.handledelete, name='handledelete'),
    path('sidenav/', views.handlesidenav, name='handlesidenav'),
    path('sidenav1/', views.handlesidenav1, name='handlesidenav1'),
    path('order/', views.handleorder, name='handleorder'),
    #path('menu/', views.handlemenu, name='handlemenu'),
    path('payment/', views.handlepay, name='handlepay'),
    path('menucard/', views.handlemenucard, name='handlemenucard'),
]