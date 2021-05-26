from django import forms
from .models import Tb_cliente, Tb_usuario, Tb_fornecedor

class TbEstoqueForm(forms.Form):
    ds_n = forms.CharField(max_length=45)
    id_produto = forms.IntegerField()
    ds_tamanho = forms.CharField(max_length=2)
    ds_cor = forms.CharField(max_length=10)
    vl_preco_custo = forms.DecimalField(max_digits=4, decimal_places=2)
    vl_preco_venda = forms.DecimalField(max_digits=4, decimal_places=2)
    dt_entrada = forms.DateField()

class TbClienteForm(forms.ModelForm):
    class Meta:
        model = Tb_cliente
        required = False
        fields = ('nome', 'cpf', 'cep', 'endereco', 'bairro', 'uf', 'dt_nascimento')

class TbUsuarioForm(forms.ModelForm):
    class Meta:
        model = Tb_usuario
        fields = ('nome', 'cpf', 'cep', 'endereco', 'email', 'telefone', 'dt_nascimento')

class TbFornecedorForm(forms.ModelForm):
    class Meta:
        model = Tb_fornecedor
        fields = ('nome', 'cnpj', 'cep', 'endereco', 'email', 'telefone', 'codigo', 'tipo')

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class Car(forms.Form):
    quantity = forms.TypedChoiceField(
        label = "Quantidade", choices=PRODUCT_QUANTITY_CHOICES, coerce=int
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )