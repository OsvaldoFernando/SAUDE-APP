from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html

# Customize the User Admin
class UserAdmin(DjangoUserAdmin):
    list_display = ('username', 'get_full_name', 'email', 'get_role', 'is_active', 'get_last_login', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    fieldsets = (
        ('Informações de Login', {'fields': ('username', 'password')}),
        ('Dados Pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )
    
    def get_role(self, obj):
        if hasattr(obj, 'profile'):
            role_map = {
                'ADMIN': '👨‍💼 Administrador',
                'DOCTOR': '👨‍⚕️ Médico',
                'RECEPTIONIST': '👨‍💻 Atendente',
            }
            return role_map.get(obj.profile.role, obj.profile.role)
        return '—'
    get_role.short_description = 'Perfil'
    
    def get_full_name(self, obj):
        return obj.get_full_name() or obj.username
    get_full_name.short_description = 'Nome Completo'
    
    def get_last_login(self, obj):
        if obj.last_login:
            return format_html('<span style="color: green;">✓ {}</span>', obj.last_login.strftime('%d/%m/%Y %H:%M'))
        return format_html('<span style="color: red;">Nunca</span>')
    get_last_login.short_description = 'Último Acesso'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Customize admin site
admin.site.site_header = "🏥 Hospital de Malanje - Painel de Administração"
admin.site.site_title = "Admin - Hospital de Malanje"
admin.site.index_title = "Bem-vindo ao Painel Administrativo"
