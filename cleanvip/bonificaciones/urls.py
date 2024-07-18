
# bonificaciones/urls.py

from django.urls import path
from .views import evaluacion_list, evaluacion_create, evaluacion_detail, bonificacion_list, bonificacion_create, bonificacion_detail

urlpatterns = [
    path('evaluaciones/', evaluacion_list, name='evaluacion_list'),
    path('evaluaciones/nueva/', evaluacion_create, name='evaluacion_create'),
    path('evaluaciones/<int:pk>/', evaluacion_detail, name='evaluacion_detail'),
    path('bonificaciones/', bonificacion_list, name='bonificacion_list'),
    path('bonificaciones/nueva/', bonificacion_create, name='bonificacion_create'),
    path('bonificaciones/<int:pk>/', bonificacion_detail, name='bonificacion_detail'),
]
