from django.urls import path
from . import views

app_name = 'test_neo'

urlpatterns = [
    path('test/', views.index, name='test')
]