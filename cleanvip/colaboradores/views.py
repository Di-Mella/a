# aplicaciones/colaboradores/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Colaborador, Genero, Departamentos, Cargo, EstadoCivil
from capacitaciones.models import Capacitacion
from .forms import ColaboradorForm

def colaboradores_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'colaboradores/colaborador_list.html', {'colaboradores': colaboradores})

def colaborador_detail(request, rut):
    colaborador = get_object_or_404(Colaborador,rut=rut)
    return render(request, 'colaboradores/colaborador_detail.html', {'colaborador': colaborador})

def colaborador_create(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('colaboradores_list')
    else:
        form = ColaboradorForm()
    return render(request, 'colaboradores/colaborador_form.html', {'form': form})

def colaborador_update(request, rut):
    colaborador = get_object_or_404(Colaborador, rut=rut)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('colaborador_detail', rut=colaborador.rut)
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'colaboradores/colaborador_form.html', {'form': form})

def colaborador_delete(request, pk):
    colaborador = get_object_or_404(Colaborador, rut=pk)
    if request.method == 'POST':
        colaborador.delete()
        return redirect('colaboradores_list')
    return render(request, 'colaboradores/colaborador_confirm_delete.html', {'colaborador': colaborador})
