# note que foi importada tb a função redirect ( não padrão )
from django.shortcuts import render, redirect
from django.contrib import messages  # permite exibir msgs ao usuario
# importa o formulário criado em forms a partir da pasta atual porisso o ponto na chamada do forms
from .forms import UserRegisterForm
# from django.contrib.auth.forms import UserCreationForm  -> comentado pois importei outro form acima
# Create your views here.


def novo_usuario(request):
    # verificar o tipo, validar, informar se foi criado ou não , salvar
    if request.method == 'POST':
        # request post pega as infrmações passadas ao site e popula as informações de usuario
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            # salvar no banco de dados
            formulario.save()
            # informar usuario
            # cleaned_data tem acesso a todas as informações inseridas no form
            usuario = formulario.cleaned_data.get('username')
            messages.success(
                request, f'O usuário {usuario} foi criado com sucesso ')
            return redirect('login')
    # caso seja criação de uma nova conta
    else:
        # formulario apresentado vazio, para entrada de informações.
        formulario = UserRegisterForm()

    return render(request, 'usuarios/registrar.html', {'formulario': formulario})
