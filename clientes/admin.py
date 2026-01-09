from django.contrib import admin
from .models import Cliente, Contrato

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['numero_cliente', 'nome', 'sexo', 'bi', 'status', 'data_cadastro']
    list_filter = ['sexo', 'status', 'data_cadastro']
    search_fields = ['numero_cliente', 'nome', 'bi', 'telefone', 'email']
    readonly_fields = ['numero_cliente', 'data_cadastro', 'data_atualizacao']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('numero_cliente', 'nome', 'sexo', 'data_nascimento')
        }),
        ('Contacto', {
            'fields': ('morada', 'telefone', 'email')
        }),
        ('Status', {
            'fields': ('status', 'observacoes')
        }),
        ('Datas', {
            'fields': ('data_cadastro', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

# ContratoAdmin removido ou desativado para Administrador não marcar consultas através de contratos
# @admin.register(Contrato)
# class ContratoAdmin(admin.ModelAdmin):
#     ...
