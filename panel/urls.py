from django.urls import path
from . import views

app_name = 'panel'

urlpatterns = [
    path('login', views.index, name='index'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('register', views.register, name='register'),
    path('', views.panel, name='panel'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('change_password', views.change_password, name='change_password'),
    path('change_picture', views.change_picture, name='change_picture'),
    path('doctors', views.doctors, name='doctors'),
    path('patients', views.patients, name='patients'),
    path('specialty', views.specialty, name='specialty'),
    path('doctor_profile/<int:id>', views.doctor_profile, name='doctor_profile'),
    path('comment/<int:id>', views.comment, name='comment'),

    # API Routes
    path('follow_api', views.follow_api, name='follow_api')
]