from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.http import HttpRequest
from .models import UserProfile, LoginAttempt, ActivityLog

User = get_user_model()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def log_activity(request, action, resource='', details=''):
    try:
        ActivityLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action=action,
            resource=resource,
            ip_address=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
            details=details
        )
    except:
        pass

@require_http_methods(["GET", "POST"])
def login_view(request):
    from .forms import LoginForm
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            ip_address = get_client_ip(request)
            
            # Log the login attempt
            try:
                LoginAttempt.objects.create(
                    username=username,
                    ip_address=ip_address,
                    user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
                    success=False
                )
            except Exception as e:
                pass
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Check if user account is active
                if not user.is_active:
                    messages.error(request, '❌ Conta desativada. Contacte o administrador do sistema.')
                    return render(request, 'auth/login.html', {'form': form})
                
                # Check user profile lock status
                if hasattr(user, 'profile'):
                    if user.profile.is_locked:
                        minutes_remaining = int((user.profile.locked_until - timezone.now()).total_seconds() / 60)
                        messages.error(request, f'🔒 Conta bloqueada por segurança. Tente novamente em {minutes_remaining} minuto(s).')
                        return render(request, 'auth/login.html', {'form': form})
                    
                    # Reset failed attempts on successful login
                    user.profile.reset_failed_attempts()
                    user.profile.last_login_ip = ip_address
                    user.profile.last_login_time = timezone.now()
                    user.profile.save()
                
                # Mark login attempt as successful
                try:
                    login_attempt = LoginAttempt.objects.filter(
                        username=username,
                        ip_address=ip_address
                    ).order_by('-timestamp').first()
                    if login_attempt:
                        login_attempt.success = True
                        login_attempt.save()
                except Exception as e:
                    pass
                
                login(request, user)
                messages.success(request, f'✅ Bem-vindo, {user.first_name or user.username}!')
                return redirect('home')
            else:
                # Failed login attempt
                try:
                    user = User.objects.get(username=username)
                    if hasattr(user, 'profile'):
                        user.profile.failed_login_attempts += 1
                        
                        # Lock account after 5 failed attempts
                        if user.profile.failed_login_attempts >= 5:
                            user.profile.locked_until = timezone.now() + timedelta(minutes=15)
                            messages.error(request, '🔒 Conta bloqueada por segurança. Tente novamente em 15 minutos.')
                        else:
                            attempts_left = 5 - user.profile.failed_login_attempts
                            messages.error(request, f'❌ Utilizador ou senha inválidos. Tem mais {attempts_left} tentativa(s).')
                        
                        user.profile.save()
                except User.DoesNotExist:
                    messages.error(request, '❌ Utilizador ou senha inválidos.')
        else:
            # Form validation errors
            pass
    
    else:
        # GET request
        form = LoginForm()
    
    return render(request, 'auth/login.html', {'form': form})

@login_required(login_url='login')
def logout_view(request):
    username = request.user.username
    logout(request)
    log_activity(request, 'LOGOUT', username)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('login')
