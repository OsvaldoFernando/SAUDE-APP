from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cliente
from .forms import PacienteForm

@login_required(login_url='login')
def paciente_list(request):
    pacientes = Cliente.objects.all()
    return render(request, 'clientes/paciente_list.html', {'pacientes': pacientes})

@login_required(login_url='login')
def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Paciente cadastrado com sucesso!')
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'clientes/paciente_form.html', {'form': form, 'title': 'Cadastrar Paciente'})

@login_required(login_url='login')
def paciente_update(request, pk):
    paciente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Dados do paciente atualizados!')
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'clientes/paciente_form.html', {'form': form, 'title': 'Editar Paciente'})

@login_required(login_url='login')
def paciente_delete(request, pk):
    paciente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, '🗑️ Paciente removido do sistema.')
        return redirect('paciente_list')
    return render(request, 'clientes/paciente_confirm_delete.html', {'paciente': paciente})
