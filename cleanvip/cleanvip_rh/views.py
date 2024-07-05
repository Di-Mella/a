from django.shortcuts import render
from .models import Departamentos,Colaborador, Capacitacion,Contrato,Evaluacion,Bonificacion,Inscripcion,Usuario,Permiso,Cargo, Ausencia,Meta,SeguimientoMeta,Indicador,DatoIndicador
# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def lista_colaboradores(request):
    colaboradores = Colaborador.objects.select_related('departamento').order_by('departamento__nombre', 'nombre')
    context = {'colaboradores': colaboradores}
    return render(request,'lista_colaboradores.html', context)

def detalle_capacitacion(request):
    capacitacion = Capacitacion.objects.all()
    context = {'capacitacion': capacitacion}
  # Renderizar la plantilla 'detalle_capacitacion.html' con el contexto
    return render(request,'detalle_capacitacion.html', context)

def lista_inscripciones(request, colaborador_id):
  # Obtener el Colaborador con la id especificada
  try:
      colaborador = Colaborador.objects.get(pk=colaborador_id)
  except Colaborador.DoesNotExist:
      # Manejar el error si el colaborador no existe
      return render(request, 'error.html')

  # Filtrar las Inscripciones para el colaborador obtenido
  inscripciones = Inscripcion.objects.filter(colaborador=colaborador)

  # Definir el contexto a pasar a la plantilla
  context = {'colaborador': colaborador, 'inscripciones': inscripciones}

  # Renderizar la plantilla 'lista_inscripciones.html' con el contexto
  return render(request, 'lista_inscripciones.html', context)

def detalle_contrato(request, pk):
  # Obtener el Contrato con la clave primaria (pk)
  try:
      contrato = Contrato.objects.get(pk=pk)
  except Contrato.DoesNotExist:
      # Manejar el error si el contrato no existe
      return render(request, 'error.html')

  # Obtener el Colaborador asociado al contrato
  colaborador = contrato.colaborador

  # Definir el contexto a pasar a la plantilla
  context = {'contrato': contrato, 'colaborador': colaborador}

  # Renderizar la plantilla 'detalle_contrato.html' con el contexto
  return render(request, 'detalle_contrato.html', context)

def lista_evaluaciones(request, contrato_id):
  # Obtener el Contrato con la id especificada
  try:
      contrato = Contrato.objects.get(pk=contrato_id)
  except Contrato.DoesNotExist:
      # Manejar el error si el contrato no existe
      return render(request, 'error.html')

  # Filtrar las Evaluaciones para el contrato obtenido
  evaluaciones = Evaluacion.objects.filter(contrato=contrato)

  # Definir el contexto a pasar a la plantilla
  context = {'contrato': contrato, 'evaluaciones': evaluaciones}

  # Renderizar la plantilla 'lista_evaluaciones.html' con el contexto
  return render(request, 'lista_evaluaciones.html', context)

def detalle_bonificacion(request, pk):
  # Obtener la Bonificacion con la clave primaria (pk)
  try:
      bonificacion = Bonificacion.objects.get(pk=pk)
  except Bonificacion.DoesNotExist:
      # Manejar el error si la bonificación no existe
      return render(request, 'error.html')

  # Obtener el Colaborador asociado a la bonificación
  colaborador = bonificacion.colaborador

  # Definir el contexto a pasar a la plantilla
  context = {'bonificacion': bonificacion, 'colaborador': colaborador}

  # Renderizar la plantilla 'detalle_bonificacion.html' con el contexto
  return render(request, 'detalle_bonificacion.html', context)

def lista_ausencias(request, colaborador_id):
  # Obtener el Colaborador con la id especificada
  try:
      colaborador = Colaborador.objects.get(pk=colaborador_id)
  except Colaborador.DoesNotExist:
      # Manejar el error si el colaborador no existe
      return render(request, 'error.html')

  # Filtrar las Ausencias para el colaborador obtenido
  ausencias = Ausencia.objects.filter(colaborador=colaborador)

  # Definir el contexto a pasar a la plantilla
  context = {'colaborador': colaborador, 'ausencias': ausencias}

  # Renderizar la plantilla 'lista_ausencias.html' con el contexto
  return render(request, 'lista_ausencias.html', context)

def lista_metas(request, colaborador_id):
  # Obtener el Colaborador con la id especificada
  try:
      colaborador = Colaborador.objects.get(pk=colaborador_id)
  except Colaborador.DoesNotExist:
      # Manejar el error si el colaborador no existe
      return render(request, 'error.html')

  # Filtrar las Metas para el colaborador obtenido
  metas = Meta.objects.filter(colaborador=colaborador)

  # Definir el contexto a pasar a la plantilla
  context = {'colaborador': colaborador, 'metas': metas}

  # Renderizar la plantilla 'lista_metas.html' con el contexto
  return render(request, 'lista_metas.html', context)

def lista_seguimiento_metas(request, meta_id):
  # Obtener la Meta con la id especificada
  try:
      meta = Meta.objects.get(pk=meta_id)
  except Meta.DoesNotExist:
      # Manejar el error si la meta no existe
      return render(request, 'error.html')

  # Filtrar los SeguimientoMetas para la meta obtenida
  seguimiento_metas = SeguimientoMeta.objects.filter(meta=meta)

  # Definir el contexto a pasar a la plantilla
  context = {'meta': meta, 'seguimiento_metas': seguimiento_metas}

  # Renderizar la plantilla 'lista_seguimiento_metas.html' con el contexto
  return render(request, 'lista_seguimiento_metas.html', context)

def lista_indicadores(request):
  # Obtener todos los Indicadores de la base de datos
  indicadores = Indicador.objects.all()

  # Definir el contexto a pasar a la plantilla
  context = {'indicadores': indicadores}

  # Renderizar la plantilla 'lista_indicadores.html' con el contexto
  return render(request, 'lista_indicadores.html', context)

def lista_datos_indicador(request, indicador_id):
  # Obtener el Indicador con la id especificada
  try:
      indicador = Indicador.objects.get(pk=indicador_id)
  except Indicador.DoesNotExist:
      # Manejar el error si el indicador no existe
      return render(request, 'error.html')

  # Filtrar los DatoIndicador para el indicador obtenido
  datos_indicador = DatoIndicador.objects.filter(indicador=indicador)

  # Definir el contexto a pasar a la plantilla
  context = {'indicador': indicador, 'datos_indicador': datos_indicador}

  # Renderizar la plantilla 'lista_datos_indicador.html' con el contexto
  return render(request, 'lista_datos_indicador.html', context)


