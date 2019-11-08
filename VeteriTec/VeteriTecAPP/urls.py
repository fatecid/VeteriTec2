
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('agenda', views.agenda, name='agenda'),

    path('calculadora', views.calculadora, name='calculadora'),

    path('clientes', views.clientes, name='clientes'),
    path('clientesbuscar', views.clientesbuscar, name='clientesbuscar'),
    path('clientes_update/<int:id>/', views.clientes_update, name='clientes_update'),
    path('clientes_delete/<int:id>/', views.clientes_delete, name='clientes_delete'),

    path('fornecedor', views.fornecedor, name='fornecedor'),
    path('fornecedorbuscar', views.fornecedorbuscar, name='fornecedorbuscar'),
    path('fornecedor_update/<int:id>/', views.fornecedor_update, name='fornecedor_update'),
    path('fornecedor_delete/<int:id>/', views.fornecedor_delete, name='fornecedor_delete'),

    path('funcionarios', views.funcionarios, name='funcionarios'),
    path('funcionariosbuscar', views.funcionariosbuscar, name='funcionariosbuscar'),
    path('funcionario_update/<int:id>/', views.funcionario_update, name='funcionario_update'),
    path('funcionario_delete/<int:id>/', views.funcionario_delete, name='funcionario_delete'),

    path('relatorio', views.relatorio, name='relatorio'),
    path('mylogout', views.mylogout, name='mylogout'),
]
