from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Empleado
from .forms import EmpleadoForm

# 1. LISTAR EMPLEADOS (Index/Read)
def index(request):
    empleados = Empleado.objects.all()
    context = {'empleados': empleados}
    return render(request, 'empleados/index.html', context)

# 2. VER DETALLES (View - Usado principalmente para redirección)
def view_empleado(request, id):
    return HttpResponseRedirect(reverse('index'))

# 3. AGREGAR EMPLEADO (Create)
def add(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'empleados/add.html', {'form': EmpleadoForm(), 'success': True})
    else:
        form = EmpleadoForm()
    
    context = {'form': form}
    return render(request, 'empleados/add.html', context)

# 4. EDITAR EMPLEADO (Update)
def edit(request, id):
    empleado = get_object_or_404(Empleado, pk=id)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return render(request, 'empleados/edit.html', {'form': form, 'success': True, 'empleado': empleado})
    else:
        form = EmpleadoForm(instance=empleado)
    
    context = {'form': form, 'empleado': empleado}
    return render(request, 'empleados/edit.html', context)

# 5. ELIMINAR EMPLEADO (Delete)
def delete(request, id):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, pk=id)
        empleado.delete()
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))