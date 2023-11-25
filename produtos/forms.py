from django import forms
from django.core.exceptions import ValidationError
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome','descricao','preco','validade')
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) <= 3:
             # aqui levanta uma exceção/erro, se tiver menor ou igual a 3 caracteres
             raise ValidationError('o campo precisa ter mais que 3 caracteres.')

        return nome