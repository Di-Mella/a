from django.contrib import admin
from django.urls import path, include
from . import views
from .views import home
urlpatterns = [
    path('',views.home, name= 'home'),
    path('registro',views.registro, name = 'registro'),
    path('login',views.loginPage, name = 'login'),
    path('logout',views.cerrar_sesion, name = 'logout'),
    path('profile/<str:username>',views.profile, name= 'profile'),
    path('profile_edit',views.profile_edit, name= 'profile_edit'),
    path('colaboradores/', include('colaboradores.urls')),
    path('contrataciones/', include('contrataciones.urls')),
    path('bonificaciones/', include('bonificaciones.urls')),
    path('evaluaciones/', include('bonificaciones.urls')),
]

