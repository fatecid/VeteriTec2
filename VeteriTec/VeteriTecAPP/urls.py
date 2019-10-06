from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('agenda', views.agenda, name='agenda'),
    path('calculadora', views.calculadora, name='calculadora'),
    path('clientes', views.clientes, name='clientes'),
    path('fornecedor', views.fornecedor, name='fornecedor'),
    path('funcionarios', views.funcionarios, name='funcionarios'),
    path('relatorio', views.relatorio, name='relatorio'),
    path('mylogout', views.mylogout, name='mylogout'),
]
