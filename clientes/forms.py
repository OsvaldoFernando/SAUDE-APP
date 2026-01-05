from django import forms
from .models import Cliente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'nif', 'bi', 'morada', 'telefone', 'email', 'tipo_cliente', 'status']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nome Completo'}),
            'nif': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'NIF'}),
            'bi': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'BI'}),
            'morada': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Endereço'}),
            'telefone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Telefone'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}),
            'tipo_cliente': forms.Select(attrs={'class': 'form-input'}),
            'status': forms.Select(attrs={'class': 'form-input'}),
        }
