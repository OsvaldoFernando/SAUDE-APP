from django.utils.deprecation import MiddlewareMixin
from .models import ActivityLog

class SecurityHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Add security headers
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
        return response

class ActivityLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Don't log static files and media
        if request.path.startswith('/static/') or request.path.startswith('/media/'):
            return None
        
        # Log specific views
        if request.user.is_authenticated and request.method in ['POST', 'PUT', 'DELETE']:
            try:
                action_map = {
                    'POST': 'CREATE',
                    'PUT': 'UPDATE',
                    'DELETE': 'DELETE',
                }
                
                ActivityLog.objects.create(
                    user=request.user,
                    action=action_map.get(request.method, 'VIEW'),
                    resource=request.path,
                    ip_address=self.get_client_ip(request),
                    user_agent=request.META.get('HTTP_USER_AGENT', '')[:500]
                )
            except:
                pass
        
        return None
    
    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
