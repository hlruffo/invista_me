from django.shortcuts import render, redirect, HttpResponse
from .models import Investimentos
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required


def investimentos(request):
    dados = {
        'dados': Investimentos.objects.all()
    }
    return render(request, "investimentos/investimentos.html", context=dados)


def detalhe(request, id_investimento):
    dados = {
        'dados': Investimentos.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)


@login_required
def criar(request):
    if request.method == "POST":
        # acessa as informações passadas na tela
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():  # a função is_valid confere se os dados estão corretamente preenchidos
            # a função save, salva os dados no banco de dados.
            investimento_form.save()
        # redireciona para url com name investimento
        return redirect('investimentos')

    else:  # acessando a pagina pela primeira vez, criar um formulario do zero
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)


@login_required
def editar(request, id_investimento):  # recebe o id_investimento como parametro
    # procura no banco de dados a chave primaria igual a id_investimentos
    investimento = Investimentos.objects.get(pk=id_investimento)
    # novo_investimento/1 -> acesso pela primeira vez -> metodo get para popular o formulario
    if request.method == "GET":
        # popula o formulario atraves das instancias ja preenchidas
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    # caso requisição seja post
    else:
        # neste caso os dados já estão preenchidos e salvos em investimento
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')  # redireciona para pagina incial


@login_required
def excluir(request, id_investimento):
    investimento = Investimentos.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {"item": investimento})
