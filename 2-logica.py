# Interface gráfica no python
# Tkinter - vem com a instalação do interpretador do python
import tkinter as tk
from pathlib import Path

CORFUNDO = "#14131a"
CORTEXTO = "#ffffff"

def registar():
    nome = nome_entry.get()
    password = password_entry.get()
    
    if password == '' or nome == '':
        msg_label.configure(text="Por favor, preencha todos os campos.", fg="red")
    else:
        ficheiro = Path(r'dados.txt')

        with ficheiro.open('w', encoding='utf-8', errors='ignore') as file:
            file.write(f"Nome: {nome}\nPassword: {password}")

        msg_label.configure(text="Dados Registados com Sucesso!", fg="green")

# 1 - Criar a variável que representa a janela
root = tk.Tk() # Cria a janela principal da interface gráfica
root.configure(bg="#14131a")  # Configura a cor de fundo da janela
root.title('1- Esqueleto da GUI') # Define o título da janela
root.geometry('600x400') # Define o tamanho da janela (largura x altura)
#root.state('zoomed') # Define o estado da janela como maximizada (preenchendo toda a tela)

# Para criar elementos (widgets) há sempre 2 passos:
# 1 - Criar a variável que representa o widget
# tk.widget(qual janela?, qual texto?)
nome_label = tk.Label(root, text="Digite o seu nome:", bg=CORFUNDO, fg=CORTEXTO, font=("Arial", 14, "bold")) # Cria um widget do tipo label (rótulo) para solicitar o nome do usuário

# 2 - Posicionar o widget na janela
nome_label.pack(pady=20)
nome_entry = tk.Entry(root) # Cria um widget do tipo entry (campo de entrada) para o usuário digitar seu nome
nome_entry.pack()

# campo para password
password_label = tk.Label(root, text="Digite a sua password:", bg=CORFUNDO, fg=CORTEXTO, font=("Arial", 12))
password_label.pack(pady=20)
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack()

# Botão
registar_button = tk.Button(root, text="Registar", bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5, command=registar)
registar_button.pack(pady=(25, 0))

# Mensagem informativa
msg_label = tk.Label(root, text="", bg=CORFUNDO, fg=CORTEXTO, font=("Arial", 20, "bold"))
msg_label.pack(pady=30)

# Por último: Iniciar o loop da interface gráfica
root.mainloop() 