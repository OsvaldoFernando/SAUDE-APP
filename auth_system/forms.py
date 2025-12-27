from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Utilizador',
        max_length=150,
        required=True,
        error_messages={
            'required': '❌ Campo Utilizador é obrigatório',
            'max_length': '❌ Utilizador não pode ter mais de 150 caracteres',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Introduza o seu utilizador',
            'autocomplete': 'username',
            'required': 'required',
            'minlength': '3',
            'maxlength': '150',
        })
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        error_messages={
            'required': '❌ Campo Senha é obrigatório',
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Introduza a sua senha',
            'autocomplete': 'current-password',
            'required': 'required',
            'minlength': '6',
        })
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if not username:
            raise ValidationError('❌ Utilizador não pode estar vazio')
        if len(username) < 3:
            raise ValidationError('❌ Utilizador deve ter pelo menos 3 caracteres')
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if not password:
            raise ValidationError('❌ Senha não pode estar vazia')
        if len(password) < 6:
            raise ValidationError('❌ Senha deve ter pelo menos 6 caracteres')
        return password

class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        label='Senha Atual',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Senha Atual',
            'autocomplete': 'current-password'
        })
    )
    new_password1 = forms.CharField(
        label='Nova Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nova Senha',
            'autocomplete': 'new-password'
        })
    )
    new_password2 = forms.CharField(
        label='Confirmar Nova Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar Nova Senha',
            'autocomplete': 'new-password'
        })
    )
    
    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')
        if password:
            try:
                validate_password(password)
            except forms.ValidationError as e:
                raise forms.ValidationError(e.messages)
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('As senhas não coincidem.')
        
        return cleaned_data
