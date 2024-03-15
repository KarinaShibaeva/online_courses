from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import register, login_view, logout_view

app_name = 'register'

urlpatterns = [
    path('', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]