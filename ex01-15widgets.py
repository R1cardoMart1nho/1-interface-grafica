print('olá mundo')

import tkinter as tk

COR_FUNDO = "#1A1A1E"
COR_TEXTO = "#C5CED3"

root = tk.Tk()
root.configure(bg=COR_FUNDO)
root.title('1 - Interface da GUI')
root.geometry('600x700')

# ---------------- LABEL + ENTRY ----------------
nome_label = tk.Label(root, text='Digite o seu nome',
                      bg=COR_FUNDO, fg=COR_TEXTO,
                      font=('Arial', 14, 'bold'))
nome_label.pack()

nome_entry = tk.Entry(root, width=30)
nome_entry.pack(pady=10)

# ---------------- PASSWORD ----------------
password_label = tk.Label(root, text='Digite a sua password',
                          bg=COR_FUNDO, fg=COR_TEXTO,
                          font=('Arial', 14, 'bold'))
password_label.pack()

password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=10)

# ---------------- BUTTON ----------------
registar_button = tk.Button(root, text="Registar",
                            bg="#4CAF50", fg="white",
                            font=("Arial", 12, "bold"))
registar_button.pack(pady=10)

# ==================================================
# OUTROS WIDGETS
# ==================================================

# ---------------- MENU ----------------
menu = tk.Menu(root, bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 12, "bold"))
root.config(menu=menu)

menubutton = tk.Menubutton(root, text="Menu" + "\u2630",
                           bg=COR_FUNDO, fg=COR_TEXTO,
                           font=("Arial", 12, "bold"),
                           relief=tk.RAISED)
menubutton.pack(pady=5)

# ---------------- SCROLLBAR ----------------
scroll = tk.Scrollbar(root)
scroll.pack(side="right", fill="y")

# ---------------- FRAME ----------------
frame = tk.Frame(root, bg="#2A2A2E", padx=10, pady=10)
frame.pack(pady=10)

tk.Label(frame, text="Isto está dentro de um Frame",
         bg="#2A2A2E", fg="white").pack()

# ---------------- LABELFRAME ----------------
labelframe = tk.LabelFrame(root, text="Preferências",
                           bg=COR_FUNDO, fg=COR_TEXTO)
labelframe.pack(pady=10)

# ---------------- CHECKBUTTON ----------------
check_var = tk.BooleanVar()
check = tk.Checkbutton(labelframe, text="Aceito os termos",
                       variable=check_var,
                       bg=COR_FUNDO, fg=COR_TEXTO,
                       selectcolor=COR_FUNDO)
check.pack()

# ---------------- RADIOBUTTON ----------------
radio_var = tk.StringVar()

radio1 = tk.Radiobutton(root, text="Masculino",
                        variable=radio_var, value="M",
                        bg=COR_FUNDO, fg=COR_TEXTO,
                        selectcolor=COR_FUNDO)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Feminino",
                        variable=radio_var, value="F",
                        bg=COR_FUNDO, fg=COR_TEXTO,
                        selectcolor=COR_FUNDO)
radio2.pack()

# ---------------- SCALE ----------------
scale = tk.Scale(root, from_=0, to=100,
                 orient="horizontal",
                 bg=COR_FUNDO, fg=COR_TEXTO)
scale.pack(pady=10)

# ---------------- SPINBOX ----------------
spin = tk.Spinbox(root, from_=0, to=10, width=5)
spin.pack(pady=5)

# ---------------- LISTBOX ----------------
listbox = tk.Listbox(root, height=3)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.pack(pady=5)

# ---------------- TEXT ----------------
text = tk.Text(root, height=3, width=30)
text.pack(pady=10)

# ---------------- CANVAS ----------------
canvas = tk.Canvas(root, width=200, height=80, bg="white")
canvas.create_oval(50, 20, 150, 70, fill="blue")
canvas.pack(pady=10)

# ---------------- PANEDWINDOW ----------------
paned = tk.PanedWindow(root, orient="horizontal")
paned.pack(fill="x", pady=10)

left = tk.Label(paned, text="Esquerda", bg="red", width=15)
right = tk.Label(paned, text="Direita", bg="blue", width=15)

paned.add(left)
paned.add(right)

# ---------------- MESSAGE ----------------
message = tk.Message(root, text="Isto é um widget Message. "
                                "Adapta o texto automaticamente.",
                     width=300,
                     bg=COR_FUNDO, fg=COR_TEXTO)
message.pack(pady=10)

# ---------------- TOPLEVEL ----------------
def abrir_janela():
    nova = tk.Toplevel(root)
    nova.title("Nova Janela")
    nova.geometry("300x200")
    tk.Label(nova, text="Isto é outra janela!").pack(pady=20)

tk.Button(root, text="Abrir Janela",
          command=abrir_janela).pack(pady=10)

# ---------------- LOOP ----------------
root.mainloop()