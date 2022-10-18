# importa o modulo de formularios nativo do Django
from django.forms import ModelForm
# importa as classes que definem a tabela de dados investimento
from .models import Investimentos


class InvestimentoForm(ModelForm):
    class Meta:  # define par o Django como o formulário deve ser criado
        model = Investimentos  # qual classe definida será representada ?
        # quais campos? pode-se definir um a um com uso de uma lista ou chamar todos como foi feito
        fields = '__all__'
