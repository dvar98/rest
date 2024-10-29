# restaurante/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('cliente/', views.index_cliente_view, name='index_cliente'),
    path('admin/', views.index_admin_view, name='index_admin'),
    path('login/cliente/', views.login_cliente_view, name='login_cliente'),
    path('registro/cliente/', views.registro_cliente_view, name='registro_cliente'),
    path('login/admin/', views.login_admin_view, name='login_admin'),
    path('registro/admin/', views.registro_admin_view, name='registro_admin'),
    path('reserva/', views.reserva_view, name='reserva'),
    path('admin/reservas/', views.admin_reserva_view, name='admin_reserva'),
]