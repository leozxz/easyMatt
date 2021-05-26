from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Tb_estoque
from .forms import TbEstoqueForm, TbClienteForm, TbUsuarioForm, TbFornecedorForm, Car


def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'account/success.html')

def unsuccessC(request):
    return render(request, 'account/unsuccess/unsuccessC.html')
def unsuccessF(request):
    return render(request, 'account/unsuccess/unsuccessF.html')
def unsuccessU(request):
    return render(request, 'account/unsuccess/unsuccessU.html')
def unsuccessV(request):
    return render(request, 'account/unsuccess/unsuccessV.html')

def cadastro(request):
    if request.method == 'POST':
        form = TbClienteForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('../success')
        else:
            return redirect('../unsuccessC')
    else:
        form = TbClienteForm()
    return render(request, 'account/cadastro.html', {'form': form})

def cadastroU(request):
    if request.method == 'POST':
        form = TbUsuarioForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('../success')
        else:
            return redirect('../unsuccessU')
    else:
        form = TbUsuarioForm()
    return render(request, 'account/cadastroU.html', {'form': form})

def cadastroF(request):
    if request.method == 'POST':
        form = TbFornecedorForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('../success')
        else:
            return redirect('../unsuccessF')
    else:
        form = TbFornecedorForm()
    return render(request, 'account/cadastroF.html', {'form': form})

def cadastroV(request):
    return render(request, 'account/cadastroV.html')

@login_required(login_url='/login/')
def produtos(request):
    if request.method == 'POST':
        form = TbEstoqueForm(request.POST)
        if form.is_valid():
            ds_n = form['ds_n'].value()
            id_produto = form['id_produto'].value()
            ds_tamanho = form['ds_tamanho'].value()
            ds_cor = form['ds_cor'].value()
            vl_preco_custo= form['vl_preco_custo'].value()
            vl_preco_venda = form['vl_preco_venda'].value()
            dt_entrada = form['dt_entrada'].value()


            cadastroProduto = Tb_estoque(ds_n=ds_n, id_produto=id_produto,ds_tamanho=ds_tamanho, vl_preco_custo=vl_preco_custo, vl_preco_venda=vl_preco_venda, dt_entrada=dt_entrada, ds_cor=ds_cor)
            cadastroProduto.save()
        else:
            messages.error(request, 'Algo deu errado!')
            return redirect('home')
    else:
        cadastroProduto = Tb_estoque.objects.all()
    return render(request, 'produtos/produto.html', {'cadastroProduto':cadastroProduto})