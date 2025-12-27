from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('DOCTOR', 'Médico'),
        ('RECEPTIONIST', 'Atendente/Recepção'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='RECEPTIONIST')
    phone = models.CharField(max_length=15, blank=True)
    department = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Perfil do Utilizador'
        verbose_name_plural = 'Perfis dos Utilizadores'

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
