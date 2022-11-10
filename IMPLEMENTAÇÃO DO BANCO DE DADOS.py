from typing import final
import psycopg2
from psycopg2 import OperationalError
import os

# Criando conexão com o banco de dados

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port)

# Tratamento das exceções
        
        print("Conexão com o banco ", db_name, " foi bem sucedida")
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")
    return connection

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executada com sucesso")
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")

# Conexão com o banco de dados Trabalhorad

connection = create_connection("postgres", "postgres", "122436","localhost", "5432")

connection.close()

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
    
# Tratamento das exceções da criação das tabelas

def create_table(connection, query):
    connection.autocommit = True
    try:
        cursor = connection.cursor()
        print("Tabela criada com sucesso!")
        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")

# Criando outra conexão com o banco de dados Trabalhorad

connection = create_connection("postgres", "postgres", "122436","localhost", "5432")

# Criação da tabela Pessoa
# O atributo adicionado foi Nacionalidade

table_Pessoa_query = """CREATE TABLE Pessoa(
    CPF char(15) PRIMARY KEY,
    Nome varchar(50) NOT NULL,
    Sobrenome varchar(50) NOT NULL,
    idade int CONSTRAINT idade_positiva CHECK (idade >= 0),
    Nacionalidade varchar(25) NOT NULL,   
    Conta varchar(30) NOT NULL
)
"""

# Criação da tabela Conta

table_Conta_query = """CREATE TABLE Conta(
    Agencia int NOT NULL,
    Numero int NOT NULL,
    Saldo int NOT NULL,
    Gerente varchar(50) NOT NULL,
    Titular varchar(50) NOT NULL,
    pessoa char REFERENCES Pessoa
)
"""

# Criação da tabela Banco

table_Banco_query = """CREATE TABLE Banco(
    CNPJ char(14) PRIMARY KEY,
    Nome varchar(40) NOT NULL,
    Apelido varchar(30) NOT NULL,
    Endereco varchar(50) NOT NULL,
    Tipo_De_Conta varchar(20) NOT NULL,
    conta char REFERENCES Conta
)
"""

create_table(connection, table_Pessoa_query)
create_table(connection, table_Conta_query)
create_table(connection, table_Banco_query)

connection.close()

connection = create_connection("postgres", "postgres", "122436","localhost", "5432")

def dql (query): # select
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    vcon.commit()
    vcon.close()
    res=c.fetchal()
    vcon.close()
    return res
    
def dql (query): # insert
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    vcon.commit()
    vcon.close()
    res=c.fetchal()
    vcon.close()
    return res

def dql (query): # update
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    vcon.commit()
    vcon.close()
    res=c.fetchal()
    vcon.close()
    return res

def dql (query): # delete
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    vcon.commit()
    vcon.close()
    res=c.fetchal()
    vcon.close()
    return res
    
connection.close()
