# contrataciones/urls.py

from django.urls import path
from .views import contratacion_list, contratacion_create, contratacion_detail

urlpatterns = [
    path('', contratacion_list, name='contratacion_list'),
    path('nueva/', contratacion_create, name='contratacion_create'),
    path('<int:pk>/', contratacion_detail, name='contratacion_detail'),
]

