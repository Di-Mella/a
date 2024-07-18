# contrataciones/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Contratacion
from .forms import ContratacionForm
from colaboradores.models import Colaborador

def contratacion_list(request):
    contrataciones = Contratacion.objects.all()
    return render(request, 'contrataciones/contratacion_list.html', {'contrataciones': contrataciones})

def contratacion_create(request):
    if request.method == 'POST':
        form = ContratacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contratacion_list')
    else:
        form = ContratacionForm()
    return render(request, 'contrataciones/contratacion_form.html', {'form': form})

def contratacion_detail(request, pk):
    contratacion = get_object_or_404(Contratacion, pk=pk)
    return render(request, 'contrataciones/contratacion_detail.html', {'contratacion': contratacion})
