from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('register', views.register, name='register'),
    path('panel', views.panel, name='panel'),
    path('profile', views.profile, name='profile'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
    path('change_password', views.change_password, name='change_password'),
    path('change_picture', views.change_picture, name='change_picture')
]