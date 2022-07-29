from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login_view', views.login_view, name='login_view'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile')
]