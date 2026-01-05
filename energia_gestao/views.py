from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from clientes.models import Cliente
from equipamentos.models import Contador
from pagamentos.models import Fatura, Recarga
from django.db.models import Sum, Count
from django.utils import timezone

@login_required(login_url='login')
def home(request):
    hoje = timezone.now().date()
    # Mapeando os modelos para a nova terminologia (Hospital)
    # Cliente -> Paciente
    # Contador -> Médico
    # Fatura -> Consulta
    # Recarga -> Agendamento
    
    context = {
        'total_pacientes': Cliente.objects.count(),
        'pacientes_ativos': Cliente.objects.filter(status='ATIVO').count(),
        'consultas_hoje': Fatura.objects.filter(data_emissao=hoje).count(),
        'consultas_atendidas': Fatura.objects.filter(status='PAGO').count(),
        'medicos_ativos': Contador.objects.filter(status='ATIVO').count(),
        'total_consultas': Fatura.objects.count(),
        'consultas_pendentes': Fatura.objects.filter(status='PENDENTE').count(),
        # Dados para o gráfico (últimos 7 dias)
        'grafico_labels': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'],
        'grafico_data': [12, 19, 3, 5, 2, 3, 10], # Placeholder - pode ser dinamizado depois
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def dashboard(request):
    context = {
        'total_pacientes': Cliente.objects.count(),
        'pacientes_ativos': Cliente.objects.filter(status='ATIVO').count(),
        'pacientes_inativos': Cliente.objects.filter(status='INATIVO').count(),
        'total_consultas': Fatura.objects.count(),
        'consultas_pendentes': Fatura.objects.filter(status='PENDENTE').count(),
        'consultas_realizadas': Fatura.objects.filter(status='PAGO').count(),
        'total_agendamentos': Recarga.objects.filter(status='CONFIRMADO').count(),
        'valor_agendamentos': Recarga.objects.filter(status='CONFIRMADO').aggregate(Sum('valor'))['valor__sum'] or 0,
        'ultimos_pacientes': Cliente.objects.all()[:5],
        'ultimas_consultas': Fatura.objects.all()[:5],
    }
    return render(request, 'dashboard.html', context)
