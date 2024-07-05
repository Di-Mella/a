from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home, name= 'home'),
    path('colaboradores/',views.lista_colaboradores, name='lista_colaboradores'),
    path('capacitacion/',views.detalle_capacitacion, name='detalle_capacitacion'),
    path('inscripciones/<int:colaborador_id>/',views.lista_inscripciones, name='lista_inscripciones'),
    path('contrato/<int:pk>/',views.detalle_contrato, name='detalle_contrato'),
    path('evaluaciones/<int:contrato_id>/',views.lista_evaluaciones, name='lista_evaluaciones'),
    path('bonificacion/<int:pk>/',views.detalle_bonificacion, name='detalle_bonificacion'),
    path('ausencias/<int:colaborador_id>/',views.lista_ausencias, name='lista_ausencias'),
    path('metas/<int:colaborador_id>/',views.lista_metas, name='lista_metas'),
    path('seguimiento_metas/<int:meta_id>/',views.lista_seguimiento_metas, name='lista_seguimiento_metas'),
    path('indicadores/',views.lista_indicadores, name='lista_indicadores'),
    path('datos_indicador/<int:indicador_id>/', views.lista_datos_indicador, name='lista_datos_indicador'),
]

