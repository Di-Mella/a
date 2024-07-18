# aplicaciones/capacitaciones/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Capacitacion
from .forms import CapacitacionForm

def capacitaciones_list(request):
    capacitaciones = Capacitacion.objects.all()
    return render(request, 'capacitaciones/capacitaciones_list.html', {'capacitaciones': capacitaciones})

def capacitacion_detail(request, pk):
    capacitacion = get_object_or_404(Capacitacion, pk=pk)
    return render(request, 'capacitaciones/capacitacion_detail.html', {'capacitacion': capacitacion})

def capacitacion_create(request):
    if request.method == 'POST':
        form = CapacitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capacitaciones_list')
    else:
        form = CapacitacionForm()
    return render(request, 'capacitaciones/capacitacion_form.html', {'form': form})

def capacitacion_update(request, pk):
    capacitacion = get_object_or_404(Capacitacion, pk=pk)
    if request.method == 'POST':
        form = CapacitacionForm(request.POST, instance=capacitacion)
        if form.is_valid():
            form.save()
            return redirect('capacitacion_detail', pk=capacitacion.pk)
    else:
        form = CapacitacionForm(instance=capacitacion)
    return render(request, 'capacitaciones/capacitacion_form.html', {'form': form})

def capacitacion_delete(request, pk):
    capacitacion = get_object_or_404(Capacitacion, pk=pk)
    if request.method == 'POST':
        capacitacion.delete()
        return redirect('capacitaciones_list')
    return render(request, 'capacitaciones/capacitacion_confirm_delete.html', {'capacitacion': capacitacion})
