from django.urls import path

from users.views import login, logout, register

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login.html'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register.html'),
]