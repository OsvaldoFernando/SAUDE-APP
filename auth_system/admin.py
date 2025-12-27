from django.contrib import admin
from .models import UserProfile, LoginAttempt, ActivityLog

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'department', 'is_active', 'failed_login_attempts', 'last_login_ip', 'last_login_time', 'created_at')
    list_filter = ('role', 'is_active', 'created_at', 'last_login_time')
    search_fields = ('user__username', 'user__email', 'department')
    readonly_fields = ('created_at', 'updated_at', 'last_login_ip', 'last_login_time', 'password_changed_at')
    
    fieldsets = (
        ('Informações do Utilizador', {
            'fields': ('user', 'role', 'is_active')
        }),
        ('Detalhes Profissionais', {
            'fields': ('department', 'phone')
        }),
        ('Segurança', {
            'fields': ('failed_login_attempts', 'locked_until', 'last_login_ip', 'last_login_time', 'password_changed_at')
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(LoginAttempt)
class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'success', 'timestamp')
    list_filter = ('success', 'timestamp')
    search_fields = ('username', 'ip_address')
    readonly_fields = ('username', 'ip_address', 'user_agent', 'success', 'timestamp')
    date_hierarchy = 'timestamp'
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'resource', 'ip_address', 'timestamp')
    list_filter = ('action', 'timestamp', 'user')
    search_fields = ('user__username', 'resource', 'ip_address')
    readonly_fields = ('user', 'action', 'resource', 'ip_address', 'user_agent', 'details', 'timestamp')
    date_hierarchy = 'timestamp'
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
