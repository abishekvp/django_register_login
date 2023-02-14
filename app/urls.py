from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("homepage/login", views.login_request, name="login"),
    path("homepage", views.homepage, name="homepage"),
    path("logout", views.logout_request, name= "logout"),
]