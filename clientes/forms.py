from django import forms
from .models import Cliente, Contrato
from django.core.exceptions import ValidationError

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'nif', 'bi', 'morada', 'telefone', 'email', 'tipo_cliente', 'status', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo', 'required': True}),
            'nif': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIF', 'required': True}),
            'bi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bilhete de Identidade', 'required': True}),
            'morada': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Morada completa', 'required': True}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (opcional)'}),
            'tipo_cliente': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'status': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observações (opcional)'}),
        }
        labels = {
            'nome': '👤 Nome Completo',
            'nif': '📋 NIF',
            'bi': '🆔 Bilhete de Identidade',
            'morada': '📍 Morada',
            'telefone': '📞 Telefone',
            'email': '📧 Email',
            'tipo_cliente': '💳 Tipo de Paciente',
            'status': '✅ Status',
            'observacoes': '📝 Observações',
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if len(nome) < 3:
            raise ValidationError('❌ Nome deve ter pelo menos 3 caracteres')
        return nome

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone', '')
        if len(telefone) < 9:
            raise ValidationError('❌ Telefone deve ter pelo menos 9 dígitos')
        return telefone


class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['cliente', 'data_inicio', 'data_fim', 'status', 'tarifa_kwh', 'observacoes']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'data_fim': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'tarifa_kwh': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'required': True}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'cliente': '👤 Paciente',
            'data_inicio': '📅 Data Início',
            'data_fim': '📅 Data Fim',
            'status': '✅ Status',
            'tarifa_kwh': '💰 Tarifa',
            'observacoes': '📝 Observações',
        }
