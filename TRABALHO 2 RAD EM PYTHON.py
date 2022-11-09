import tkinter as tk
import os
import tkinter.messagebox


#Criando Janela Menu
janelamenu = tk.Tk()
janelamenu.title("Menu")
janelamenu.geometry('300x270+800+300')
janelamenu.minsize(300,270)
janelamenu.maxsize(300,270)

def criarArquivo():
    def btnStitulo(): # Função Criar Arquivo
        print(NomeArquivo.get())
        open(str(NomeArquivo.get()),"w")

    def inserindoDados(): # Função Inserir Dados
        def aprentarDados(): # Função apresentar dados escritos para o usuário
            # Criando Janela Apresentar
            janelaapresentar = tk.Toplevel()
            janelaapresentar.title("Dados Salvos")
            janelaapresentar.geometry('300x270+800+300')
            janelaapresentar.minsize(300, 270)
            janelaapresentar.maxsize(300, 270)

            # Abrindo Arquivo
            Arquivo = NomeArquivo.get()
            with open(Arquivo, 'r+', encoding="utf-8") as Ler:
                Linha = Ler.readlines()
                print(Linha[0])
                print(Linha[1])
                print(Linha[2])
                print(Linha[3])
                print(Linha[4])
                print(Linha[5])
                print(Linha[6])
                print(Linha[7])
                print(Linha[8])
                print(Linha[9])

            # Parte para Apresentação ao usuário
            A = tk.Label(janelaapresentar,text="Os dados foram salvos como:")
            A.grid(row=0,column=0)
            B = tk.Label(janelaapresentar, text="-------------")
            B.grid(row=0, column=1)
            C = tk.Label(janelaapresentar, text="Dados Inseridos:")
            C.grid(row=3, column=0)
            D = tk.Label(janelaapresentar, text="-------------")
            D.grid(row=4, column=0)
            E = tk.Label(janelaapresentar, text="-------------")
            E.grid(row=5, column=0)
            F = tk.Label(janelaapresentar, text="-------------")
            F.grid(row=6, column=0)
            G = tk.Label(janelaapresentar, text="-------------")
            G.grid(row=7, column=0)
            H = tk.Label(janelaapresentar, text="-------------")
            H.grid(row=8, column=0)
            I = tk.Label(janelaapresentar, text="-------------")
            I.grid(row=9, column=0)
            J = tk.Label(janelaapresentar, text="-------------")
            J.grid(row=10, column=0)
            K = tk.Label(janelaapresentar, text="-------------")
            K.grid(row=11, column=0)
            L = tk.Label(janelaapresentar, text="-------------")
            L.grid(row=12, column=0)
            M = tk.Label(janelaapresentar, text="-------------")
            M.grid(row=13, column=0)

            B["text"] = NomeArquivo.get()
            D["text"] = Linha[0].rstrip("\n")
            E["text"] = Linha[1].rstrip("\n")
            F["text"] = Linha[2].rstrip("\n")
            G["text"] = Linha[3].rstrip("\n")
            H["text"] = Linha[4].rstrip("\n")
            I["text"] = Linha[5].rstrip("\n")
            J["text"] = Linha[6].rstrip("\n")
            K["text"] = Linha[7].rstrip("\n")
            L["text"] = Linha[8].rstrip("\n")
            M["text"] = Linha[9].rstrip("\n")

            tk.Button(janelaapresentar, text="Voltar o menu", command=lambda:[janelaapresentar.destroy(),janelacriar.destroy(),janelainserir.destroy()]).grid(row=13, column=1)


        def btnSdados(): # Função salvar dados no arquivo txt criado
                    print(f"{cpf_bd.get()}\n{nome_bd.get()}\n{sobrenome_bd.get()}\n{idade_bd.get()}\n{conta_bd.get()}\n{agencia_bd.get()}\n{numero_bd.get()}\n{saldo_bd.get()}\n{gerente_bd.get()}\n{titular_bd.get()}")
                    Arquivo = NomeArquivo.get()
                    CPF = cpf_bd.get()
                    NOME = nome_bd.get()
                    SOBRENOME = sobrenome_bd.get()
                    IDADE = idade_bd.get()
                    CONTA = conta_bd.get()
                    AGENCIA = agencia_bd.get()
                    NUMERO = numero_bd.get()
                    SALDO = saldo_bd.get()
                    GERENTE = gerente_bd.get()
                    TITULAR = titular_bd.get()
                    with open(Arquivo, 'w', encoding="utf-8") as Salvar:
                        Salvar.write("|CPF: "+ CPF + "\n")
                        Salvar.write("|Nome: " + NOME + "\n")
                        Salvar.write("|Sobrenome: " + SOBRENOME + "\n")
                        Salvar.write("|Idade: " + IDADE + "\n")
                        Salvar.write("|Conta: " + CONTA + "\n")
                        Salvar.write("|Agencia: " + AGENCIA + "\n")
                        Salvar.write("|Numero: " + NUMERO + "\n")
                        Salvar.write("|Saldo: " + SALDO + "\n")
                        Salvar.write("|Gerente: " + GERENTE + "\n")
                        Salvar.write("|Titular: " + TITULAR + "\n")

