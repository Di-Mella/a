# bonificaciones/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Evaluacion, Bonificacion
from .forms import EvaluacionForm, BonificacionForm
from colaboradores.models import Colaborador

def evaluacion_list(request):
    evaluaciones = Evaluacion.objects.all()
    return render(request, 'bonificaciones/evaluacion_list.html', {'evaluaciones': evaluaciones})

def evaluacion_create(request):
    if request.method == 'POST':
        form = EvaluacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evaluacion_list')
    else:
        form = EvaluacionForm()
    return render(request, 'bonificaciones/evaluacion_form.html', {'form': form})

def evaluacion_detail(request, pk):
    evaluacion = get_object_or_404(Evaluacion, pk=pk)
    return render(request, 'bonificaciones/evaluacion_detail.html', {'evaluacion': evaluacion})

def bonificacion_list(request):
    bonificaciones = Bonificacion.objects.all()
    return render(request, 'bonificaciones/bonificacion_list.html', {'bonificaciones': bonificaciones})

def bonificacion_create(request):
    if request.method == 'POST':
        form = BonificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bonificacion_list')
    else:
        form = BonificacionForm()
    return render(request, 'bonificaciones/bonificacion_form.html', {'form': form})

def bonificacion_detail(request, pk):
    bonificacion = get_object_or_404(Bonificacion, pk=pk)
    return render(request, 'bonificaciones/bonificacion_detail.html', {'bonificacion': bonificacion})
