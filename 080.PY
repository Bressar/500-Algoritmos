# Algoritmo 080
# cartão de crédito - gravar os dados em um banco de dados e poder imprimi-los em uma impressora

import sqlite3
import customtkinter as ctk
from tkinter import messagebox
import re
import win32print
import win32ui
from tkinter import simpledialog












# definição de interface (UI)
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')


# função criar banco de dados
def inicializar_banco():
    conexao = sqlite3.connect('database/clientes.db')
    cursor = conexao.cursor()   
    # criar tabela, se não existir
    cursor.execute(''' create table if not exists clientes(
                        id integer primary key autoincrement,
                        nome text not null,
                        numero text not null,
                        validade text not null,
                        CVV text not null
                    )'''
                )
    conexao.commit()
    conexao.close()
 
    
# função adicionar cliente
def adicionar_cliente(cliente):
    conexao = sqlite3.connect('database/clientes.db')
    cursor = conexao.cursor()    
    cursor.execute("INSERT INTO clientes (nome, numero, validade, CVV) VALUES (?, ?, ?, ?)",
                 (cliente['nome'], cliente['número'], cliente['data_validade'], cliente['CVV']))
    conexao.commit()
    conexao.close()
  
    
# inicialização do banco
inicializar_banco()


# Entrada e validação de dados
def capturar_dados():
    nome = entry_nome.get().strip().upper()
    numero = entry_numero.get().strip()
    validade = entry_validade.get().strip()
    cvv = entry_cvv.get().strip()
    
    # validação das entradas
    if not nome or re.search(r'\d', nome):
        messagebox.showerror('Erro', 'Nome inválido. Não deve conter números.')
        return
    if len(numero) != 16 or not numero.isdigit():
        messagebox.showerror("Erro", "Número do cartão inválido. Deve conter 16 dígitos.")
        return
    if not re.match(r'^(0[1-9]|1[0-2])/\d{2}$', validade):
        messagebox.showerror('Erro', "Validade inválida. Use o formato MM/AA.")
        return
    if len(cvv) != 3 or not cvv.isdigit():
        messagebox.showerror('Erro', "CVV inválido, Debe conter 3 dígitos.")
        return
    
    # salvando no banco de dados
    cliente = {'nome': nome, 'número': numero, 'data_validade': validade, 'CVV': cvv}
    adicionar_cliente(cliente)   
    messagebox.showinfo("Sucesso", "Dados do cliente salvos com sucesso!")
    limpar_campos() # reset dos dados
 
    
# função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, ctk.END)
    entry_numero.delete(0, ctk.END)
    entry_validade.delete(0, ctk.END)
    entry_cvv.delete(0, ctk.END)
    
    
# Interface Gráfica
app = ctk.CTk()
app.title('Cadastro de Cartão de Crédito')
app.geometry('400X400')

label_nome =ctk.CTkLabel(app, text='Nome do Cliente:')
label_nome.pack(pady=10)
entry_nome = ctk.CTkEntry(app)
entry_nome.pack(pady=10)

label_numero = ctk.CTkLabel(app, text='Número do Cartão:')
label_numero.pack(pady=10)
entry_numero = ctk.CTkEntry(app)
entry_numero.pack(pady=10)

label_validade = ctk.CTkLabel(app, text='Validade (MM/AA):')
label_validade.pack(pady=10)
entry_validade = ctk.CTkEntry(app)
entry_validade.pack(pady=10)

label_cvv = ctk.CTkLabel(app, text='CVV:')
label_cvv.pack(pady=10)
entry_cvv = ctk.CTkEntry(app)
entry_cvv.pack(pady=10)

btn_salvar = ctk.CTkButton(app, text="Salvar Dados", command=capturar_dados)
btn_salvar.pack(pady=20)

app.mainloop()


