from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('login/', views.login, name='login'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('lodge/', views.lodge, name='lodge'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('response/', views.response, name='response'),
    path('register', views.register, name='register'),
    path('panel/', views.panel, name='panel'),
    path('customer_login/', views.customer_login, name='customer_login'),
]