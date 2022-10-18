"""projeto_invista_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from invista_me import views
# como já há um views criamos um alias para o novo views de usuario
from usuarios import views as usuario_views
# views relacionadas a autenticação de usuario
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # cria a rota para novo usuario
    path('conta/', usuario_views.novo_usuario, name="novo_usuario"),
    # importa um template baseado na classe loginview (class based view). o parametro deve ser a rota de busca o template html. Se não definido será considerado registraion/login
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    # importa um template baseado na classe logoutview (class based view).o parametro deve ser a rota de busca o template html. Se não definido será considerado registraion/logout
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('', views.investimentos, name='investimentos'),
    path('novo_investimento/', views.criar, name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>', views.editar, name='editar'),
    path('excluir_investimento/<int:id_investimento>',
         views.excluir, name='excluir'),
    path('/<int:id_investimento>', views.detalhe, name='detalhe')
]
