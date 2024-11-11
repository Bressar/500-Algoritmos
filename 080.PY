# Algoritmo 080
# Cartão de crédito - parte 2 - gravar dados em um BD e imprimi-los em uma impressora(windows)

import sqlite3
import customtkinter as ctk
from tkinter import messagebox
import re
import win32print
import win32ui
from tkinter import simpledialog


# Variável global para armazenar o cliente atual
cliente = {}

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
    global cliente  # Declarando cliente como global para evitar escopo local
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
    
    
# listar impressoras (Windows)
def listar_impressoras():
    impressoras = [printer[2] for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)]
    return impressoras

# selecionar impressora com menu suspenso
def selecionar_impressora():
    impressoras = listar_impressoras()
    
    # Janela pop-up para seleção de impressora
    popup = ctk.CTkToplevel(app)
    popup.title("Selecionar Impressora")
    popup.geometry("300x200")
    
    label = ctk.CTkLabel(popup, text="Escolha uma impressora:")
    label.pack(pady=10)
    
    impressora_selecionada = ctk.StringVar(popup)
    impressora_menu = ctk.CTkOptionMenu(popup, variable=impressora_selecionada, values=impressoras)
    impressora_menu.pack(pady=20)
    
    def confirmar_selecao():
        if impressora_selecionada.get():  # Verifica se a impressora foi selecionada
            popup.destroy()
            imprimir_dados(impressora_selecionada.get())
        else:
            messagebox.showerror("Erro", "Nenhuma impressora foi selecionada.")

    
    btn_confirmar = ctk.CTkButton(popup, text="Confirmar", command=confirmar_selecao)
    btn_confirmar.pack(pady=10)
    

# função p/ imprimir os dados do cliente
def imprimir_dados(impressora):
    if not cliente:
        messagebox.showerror("Erro", "Nenhum cliente disponível para imprimir.")
        return
    
    if impressora:
        # configura a impressora escolhida
        win32print.SetDefaultPrinter(impressora)
        
        # cria interface de dispositivo para impressão
        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(impressora)
        
        # define tamanho e posição  da página
        hDC.StartDoc('Cartão de Crédito - Dados do Cliente')
        hDC.StartPage()

        # Dados a serem impressos
        texto_impresso = f"""
        Nome: {cliente['nome']}
        Número: {cliente['número']}
        Validade: {cliente['data_validade']}
        CVV: {cliente['CVV']}
        """

        # Imprime o texto (em coordenadas 100,100)
        hDC.TextOut(100, 100, texto_impresso)
        
        # Finaliza a impressão
        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()
        
        print("Documento enviado para a impressora.")
    else:
        print("Nenhuma impressora selecionada.")

    
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

btn_imprimir = ctk.CTkButton(app, text="Imprimir Dados", command=selecionar_impressora)
btn_imprimir.pack(pady=20)


app.mainloop()


""" 
# Funções para usar o setup do windows na hora da impressão, depois eu implemento


import ctypes
import win32print
import win32ui

# Exibir diálogo de impressão do Windows
def exibir_dialogo_impressao():
    printer_name = win32print.GetDefaultPrinter()  # Seleciona a impressora padrão
    # Adquire o Device Context (DC) da impressora padrão
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)
    
    # Define configurações de impressão
    devmode = hDC.GetDeviceCaps(win32print.DM_PAPERSIZE | win32print.DM_ORIENTATION)
    
    # Configurações do Page Setup (orientação, tamanho de papel)
    devmode.PaperSize = win32print.DMPAPER_A4  # A4 é um exemplo, consulte a documentação para mais
    devmode.Orientation = win32print.DMORIENT_LANDSCAPE  # Alternativa: DMORIENT_PORTRAIT
    
    # Aplica as configurações
    hDC.StartDoc("Documento para Impressão com Configurações PPD")
    hDC.StartPage()
    
    # Seu código para imprimir texto ou conteúdo aqui
    texto_impresso = "Exemplo de impressão"
    hDC.TextOut(100, 100, texto_impresso)
    
    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()

# Função para chamar a impressão
def imprimir_dados():
    exibir_dialogo_impressao()  # Chama o diálogo com as configurações do Page Setup
 """