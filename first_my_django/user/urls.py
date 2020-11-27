from django.urls import path
from .views import login, register, home, logout


urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('logout', logout, name="logout"),
]