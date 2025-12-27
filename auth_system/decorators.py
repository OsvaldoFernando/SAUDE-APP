from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, 'Por favor, faça login primeiro.')
                return redirect('login')
            
            if hasattr(request.user, 'profile') and request.user.profile.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            
            messages.error(request, 'Você não tem permissão para acessar esta página.')
            return redirect('home')
        
        return wrapper
    return decorator

def admin_required(view_func):
    return role_required(['ADMIN'])(view_func)

def doctor_required(view_func):
    return role_required(['DOCTOR'])(view_func)

def receptionist_required(view_func):
    return role_required(['RECEPTIONIST', 'ADMIN'])(view_func)
