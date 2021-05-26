# Generated by Django 3.1.4 on 2020-12-08 12:23

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_remove_tb_estoque_tx_lucro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('cep', models.IntegerField(max_length=8, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('uf', models.CharField(max_length=2, verbose_name='Uf')),
                ('dt_nascimento', models.DateField(verbose_name='Data de nascimento')),
            ],
        ),
    ]
