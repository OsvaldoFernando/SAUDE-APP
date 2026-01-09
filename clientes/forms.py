from django import forms
from .models import Cliente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sexo', 'data_nascimento', 'bi', 'telefone', 'morada', 'email', 'status']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nome Completo'}),
            'sexo': forms.Select(attrs={'class': 'form-input'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'bi': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'BI'}),
            'telefone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Telefone'}),
            'morada': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Endereço'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}),
            'status': forms.Select(attrs={'class': 'form-input'}),
        }
