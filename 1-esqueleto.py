# Interface gráfica no python
# Tkinter - vem com a instalação do interpretador do python
import tkinter as tk

COR_FUNDO = "#1A1A1E"
COR_TEXTO = "#C5CED3"

# Criar a variável que representa a janela
root = tk.Tk()
root.configure(bg=COR_FUNDO) # mudar a cor da janela
root.title('1 - Interface da GUI') # mudar o titulo
root.geometry('600x400') # configura altura e largura
# root.state('zoomed') inicia a janela maximizada

# Para criar os elementos (widgets) há sempre dois passos:
# 1 - criar a variável que representa o widget
# tk.widget(janela, texto)
nome_label = tk.Label(root,text='Digite o seu nome', bg=COR_FUNDO, fg = COR_TEXTO,
                      font=('Arial', 14, 'bold'))

# 2 - posicionar o widget na janela
nome_label.pack()
nome_entry = tk.Entry(root, width=30)
nome_entry.pack(pady=20)


# Campo para password
password_label = tk.Label(root,text='Digite a sua password', bg=COR_FUNDO, fg = COR_TEXTO, font=('Arial', 14, 'bold'))
password_label.pack()
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady = 20)

# Botão
registar_button = tk.Button(root, text="Registar", bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
registar_button.pack(pady=(25, 0))

# Iniciar o ciclo de eventos, ou seja, abrir a janela
root.mainloop()