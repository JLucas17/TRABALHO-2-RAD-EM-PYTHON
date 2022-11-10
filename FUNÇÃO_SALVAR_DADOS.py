mport psycopg2
from psycopg2 import OperationalError
import tkinter as tk
import os
import Trabalhorad

pastaApp=os.path.dirname(__file__)
nomeBanco=pastaApp+"\\trabalhorad.db"

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port)
        print("Conexão com o banco ", db_name, " foi bem sucedida")
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")
    return connection

connection = create_connection("postgres", "postgres", "122436","localhost", "5432")

# Função para Gravar: "Pessoa"

def Gravar Dados()
    if db_nome.get()!= ""
    CPF = cpf_bd.get()
    NOME = nome_bd.get()
    SOBRENOME = sobrenome_bd.get()
    IDADE = idade_bd.get()
    CONTA = conta_bd.get()
    vobs=db_obs.get("1.0", END)
    vquery="INSET INTO bd_pessoa (BD_CPF, BD_NOME, BD_SOBRENOME, BD_IDADE, BD_CONTA, BD_OBS) VALUES ('"++"', '"++"','"++"','"++"','"++"')"
    bd_cpf.delete(0, END)
    bd_nome.delete(0, END)
    bd_sobrenome.delete(0, END)
    bd_idade.delete(0, END)
    bd_conta.delete(0, END)
    print("Dados Gravados")
else:
    print("Erro")

    # Função para Gravar: "Conta"

def Gravar Dados()
    if bd_nome.get()!= ""
    AGENCIA = agencia_bd.get()
    NUMERO = numero_bd.get()
    SALDO = saldo_bd.get()
    GERENTE = gerente_bd.get()
    TITULAR = titular_bd.get()
    vobs=db_obs.get("1.0", END)
    vquery="INSET INTO bd_pessoa (BD_AGENCIA, BD_NUMERO, BD_SALDO, BD_GERENTE, BD_TITULAR, BD_OBS) VALUES ('"++"', '"++"','"++"','"++"','"++"')"
    bd_agencia.delete(0, END)
    bd_numero.delete(0, END)
    bd_saldo.delete(0, END)
    bd_gerente.delete(0, END)
    bd_titular.delete(0, END)
    print("Dados Gravados")
else:
    print("Erro")

# Função para Gravar: "Banco"

def Gravar Dados()
    if bd_nome.get()!= ""
    CNPJ = cnpj_bd.get()
    NOME_DO_BANCO = nome_do_banco_bd.get()
    APELIDO = apelido_bd.get()
    ENDERECO = endereco_bd.get()
    vobs=db_obs.get("1.0", END)
    vquery="INSET INTO bd_pessoa (BD_CNPJ, BD_NOME-DO_BANCO, BD_APELIDO, BD_ENDERECO, BD_OBS) VALUES ('"++"', '"++"','"++"','"++"')"
    bd_cnpj.delete(0, END)
    bd_nome_do_banco.delete(0, END)
    bd_apelido.delete(0, END)
    bd_endereco.delete(0, END)
    print("Dados Gravados")
else:
    print("Erro")

connection.close()