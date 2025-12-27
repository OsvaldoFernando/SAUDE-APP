from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Cliente, Contrato
from .forms import ClienteForm, ContratoForm
from auth_system.decorators import role_required

@login_required(login_url='login')
@role_required(['ADMIN', 'RECEPTIONIST', 'DOCTOR'])
def pacientes_list(request):
    """List all patients with search and filter functionality"""
    queryset = Cliente.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        queryset = queryset.filter(
            Q(nome__icontains=search_query) |
            Q(numero_cliente__icontains=search_query) |
            Q(nif__icontains=search_query) |
            Q(bi__icontains=search_query) |
            Q(telefone__icontains=search_query)
        )
    
    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        queryset = queryset.filter(status=status_filter)
    
    # Filter by type
    tipo_filter = request.GET.get('tipo', '')
    if tipo_filter:
        queryset = queryset.filter(tipo_cliente=tipo_filter)
    
    # Pagination
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'pacientes': page_obj.object_list,
        'search_query': search_query,
        'status_filter': status_filter,
        'tipo_filter': tipo_filter,
        'total_pacientes': queryset.count(),
        'status_choices': Cliente.STATUS_CHOICES,
        'tipo_choices': Cliente.TIPO_CLIENTE_CHOICES,
    }
    
    return render(request, 'clientes/pacientes_list.html', context)


@login_required(login_url='login')
@role_required(['ADMIN', 'RECEPTIONIST'])
def paciente_create(request):
    """Create a new patient"""
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            paciente = form.save()
            messages.success(request, f'✅ Paciente {paciente.nome} registado com sucesso!')
            return redirect('paciente_detail', pk=paciente.pk)
        else:
            messages.error(request, '❌ Erro ao registar paciente. Verifique os dados.')
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/paciente_form.html', {'form': form, 'title': 'Novo Paciente'})


@login_required(login_url='login')
@role_required(['ADMIN', 'RECEPTIONIST', 'DOCTOR'])
def paciente_detail(request, pk):
    """View patient details"""
    paciente = get_object_or_404(Cliente, pk=pk)
    contratos = paciente.contratos.all()
    
    context = {
        'paciente': paciente,
        'contratos': contratos,
    }
    
    return render(request, 'clientes/paciente_detail.html', context)


@login_required(login_url='login')
@role_required(['ADMIN', 'RECEPTIONIST'])
def paciente_update(request, pk):
    """Edit patient information"""
    paciente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ Paciente {paciente.nome} atualizado com sucesso!')
            return redirect('paciente_detail', pk=paciente.pk)
        else:
            messages.error(request, '❌ Erro ao atualizar paciente.')
    else:
        form = ClienteForm(instance=paciente)
    
    return render(request, 'clientes/paciente_form.html', {'form': form, 'paciente': paciente, 'title': 'Editar Paciente'})


@login_required(login_url='login')
@role_required(['ADMIN'])
def paciente_delete(request, pk):
    """Delete a patient (admin only)"""
    paciente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        nome = paciente.nome
        paciente.delete()
        messages.success(request, f'✅ Paciente {nome} eliminado com sucesso!')
        return redirect('pacientes_list')
    
    return render(request, 'clientes/paciente_confirm_delete.html', {'paciente': paciente})


@login_required(login_url='login')
@role_required(['ADMIN', 'DOCTOR'])
def contratos_list(request, paciente_pk):
    """List contracts for a patient"""
    paciente = get_object_or_404(Cliente, pk=paciente_pk)
    contratos = paciente.contratos.all()
    
    context = {
        'paciente': paciente,
        'contratos': contratos,
    }
    
    return render(request, 'clientes/contratos_list.html', context)


@login_required(login_url='login')
@role_required(['ADMIN', 'RECEPTIONIST'])
def contrato_create(request, paciente_pk):
    """Create a new contract for a patient"""
    paciente = get_object_or_404(Cliente, pk=paciente_pk)
    
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            contrato = form.save()
            messages.success(request, f'✅ Contrato criado com sucesso!')
            return redirect('paciente_detail', pk=paciente_pk)
        else:
            messages.error(request, '❌ Erro ao criar contrato.')
    else:
        form = ContratoForm(initial={'cliente': paciente})
    
    return render(request, 'clientes/contrato_form.html', {'form': form, 'paciente': paciente})
