from django.urls import path
from . import views

app_name = 'test_neo'

urlpatterns = [
    path('test/', views.index, name='test'),
    path('show_results/<str:id>', views.show_results, name='show_results'),
    path('add_advice/<str:test_id>', views.add_advice, name='add_advice'),

    # API Routes
    path('test_results/', views.test_results, name='test_results'),
    path('send_results/', views.send_results, name='send_results')
]