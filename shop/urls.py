from django.contrib import admin
from django.urls import path

from .import views


urlpatterns = [

    path('', views.helloworld, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup_user, name="signup"),
    path('product/<int:pk>', views.product, name="product"),
    path('category/<str:cat>', views.category, name="category"),
    path('category/', views.category_summery, name="category_summery"),
    path('update_user/', views.update_user, name="update_user"),
    path('update_password/', views.update_password, name="update_password"),



    

]