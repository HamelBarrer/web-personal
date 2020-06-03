from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('cerrar_sesion', views.logout_view, name='logout'),
    path('registrarse/', views.register_view, name='register'),
]
