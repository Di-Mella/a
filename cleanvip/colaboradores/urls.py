# aplicaciones/colaboradores/urls.py

from django.urls import path, include
from .views import colaboradores_list, colaborador_detail, colaborador_create, colaborador_update, colaborador_delete

urlpatterns = [
    path('list/', colaboradores_list, name='colaboradores_list'),
    path('<str:rut>/', colaborador_detail, name='colaborador_detail'),
    path('nuevo/', colaborador_create, name='colaborador_create'),
    path('<str:rut>/editar/', colaborador_update, name='colaborador_update'),
    path('<str:pk>/eliminar/', colaborador_delete, name='colaborador_delete'),
    path('contrataciones/', include('contrataciones.urls')),
    path('bonificaciones/', include('bonificaciones.urls')),
    path('evaluaciones/', include('bonificaciones.urls')),
    path('capatitaciones/', include('capacitaciones.urls')),
]
