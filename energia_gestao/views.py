from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from clientes.models import Cliente
from equipamentos.models import Contador
from pagamentos.models import Fatura, Recarga
from django.db.models import Sum, Count
from django.utils import timezone

def home(request):
    hoje = timezone.now().date()
    context = {
        'total_clientes': Cliente.objects.count(),
        'clientes_ativos': Cliente.objects.filter(status='ATIVO').count(),
        'clientes_pre_pago': Cliente.objects.filter(tipo_cliente='PRE_PAGO').count(),
        'clientes_pos_pago': Cliente.objects.filter(tipo_cliente='POS_PAGO').count(),
        'total_contadores': Contador.objects.count(),
        'contadores_ativos': Contador.objects.filter(status='ATIVO').count(),
        'faturas_pendentes': Fatura.objects.filter(status='PENDENTE').count(),
        'recargas_hoje': Recarga.objects.filter(data_recarga__date=hoje).count(),
    }
    return render(request, 'home.html', context)

def dashboard(request):
    context = {
        'total_clientes': Cliente.objects.count(),
        'clientes_ativos': Cliente.objects.filter(status='ATIVO').count(),
        'clientes_inativos': Cliente.objects.filter(status='INATIVO').count(),
        'total_faturas': Fatura.objects.count(),
        'faturas_pendentes': Fatura.objects.filter(status='PENDENTE').count(),
        'faturas_pagas': Fatura.objects.filter(status='PAGO').count(),
        'total_recargas': Recarga.objects.filter(status='CONFIRMADO').count(),
        'valor_recargas': Recarga.objects.filter(status='CONFIRMADO').aggregate(Sum('valor'))['valor__sum'] or 0,
        'ultimos_clientes': Cliente.objects.all()[:5],
        'ultimas_faturas': Fatura.objects.all()[:5],
    }
    return render(request, 'dashboard.html', context)
