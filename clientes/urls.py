from django.urls import path
from . import views

urlpatterns = [
    path('', views.pacientes_list, name='pacientes_list'),
    path('novo/', views.paciente_create, name='paciente_create'),
    path('<int:pk>/', views.paciente_detail, name='paciente_detail'),
    path('<int:pk>/editar/', views.paciente_update, name='paciente_update'),
    path('<int:pk>/eliminar/', views.paciente_delete, name='paciente_delete'),
    path('<int:paciente_pk>/contratos/', views.contratos_list, name='contratos_list'),
    path('<int:paciente_pk>/contrato-novo/', views.contrato_create, name='contrato_create'),
]
