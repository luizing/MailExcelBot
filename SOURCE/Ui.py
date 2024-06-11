import tkinter as tk
from tkinter import filedialog, messagebox
import data.GerenciarArquivo as ca

#Interface de usuário

caminho = ""
def Interface():

    # Funcionalidade dos botões

    # Escolhe o caminho do arquivo a ser enviado
    def selecionarArquivo():
        global caminho
        caminho = filedialog.askopenfilename()
        if caminho:
            arquivoSelecionado.config(text=f"Arquivo selecionado: {caminho}")

    # Confirma as informações inseridas na janela e as envia para as próximas funcoes
    def confirmar():
        if not caminho:
            messagebox.showerror("Selecione o arquivo")

        else:
            try:
                email = email_entry.get()
                primeira = int(entry1.get())
                ultima = int(entry2.get())

                if primeira > ultima:
                    messagebox.showerror("Erro de entrada")
                else:
                    ca.Gerenciamento(caminho,primeira,ultima,email)

                    root.destroy()
            except ValueError:
                messagebox.showerror("Erro de entrada")


    # Cria a janela principal
    root = tk.Tk()
    root.title("Informacoes")
    root.geometry("400x220")
    root.resizable(False, False)

    # Widget para receber caminho do arquivo
    arquivoSelecionado = tk.Label(root, text="")
    arquivoSelecionado.pack()

    selecionarArquivoButton = tk.Button(root, text="Selecionar arquivo", command=selecionarArquivo)
    selecionarArquivoButton.pack(pady=(0,0))

    # Widgets para obter linhas
    label1 = tk.Label(root, text="Primeira linha:")
    label1.pack()
    entry1 = tk.Entry(root, width=5)
    entry1.pack()

    label2 = tk.Label(root, text="Última linha:")
    label2.pack()
    entry2 = tk.Entry(root, width=5)
    entry2.pack()

    # Widgets para receber email
    email_label = tk.Label(root, text="Email:")
    email_label.pack(pady=(0,0))

    email_entry = tk.Entry(root, width=30)
    email_entry.pack(pady=(0,0))

    # Botão de confirmar (seguir para o backend)
    confirmar_button = tk.Button(root, text="Confirmar", command=confirmar)
    confirmar_button.pack(pady=(5,0))

    # Executa o loop principal
    root.mainloop()

# Chama a função que contém todas as funcionalidades
Interface()