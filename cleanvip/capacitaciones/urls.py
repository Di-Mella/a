# aplicaciones/capacitaciones/urls.py

from django.urls import path
from .views import capacitaciones_list, capacitacion_detail, capacitacion_create, capacitacion_update, capacitacion_delete

urlpatterns = [
    path('', capacitaciones_list, name='capacitaciones_list'),
    path('<int:pk>/', capacitacion_detail, name='capacitacion_detail'),
    path('nuevo/', capacitacion_create, name='capacitacion_create'),
    path('<int:pk>/editar/', capacitacion_update, name='capacitacion_update'),
    path('<int:pk>/eliminar/', capacitacion_delete, name='capacitacion_delete'),
]
