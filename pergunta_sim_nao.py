import tkinter as tk
import random


def sim_ou_nao(pergunta):
    def on_sim():
        global resposta
        resposta = True
        root.destroy()

    def mover_botao_nao(event):
        
        novo_x = random.randint(0, 150)  
        novo_y = random.randint(0, 150)
        button_nao.place(x=novo_x, y=novo_y)

    root = tk.Tk()
    root.title("Pergunta")
    root.geometry("200x200")  

    
    root.configure(bg='white')  

   
    label = tk.Label(root, text=pergunta, padx=10, pady=10, bg='white')  
    label.pack()

   
    button_sim = tk.Button(root, text="Sim", command=on_sim, bg='green', fg='white')  
    button_sim.pack(pady=10)

    
    button_nao = tk.Button(root, text="não", bg='red', fg='white')  
    button_nao.place(x=50, y=50)  
    button_nao.bind("<Enter>", mover_botao_nao)  

    root.mainloop()

    return resposta


pergunta = "tu comeria um viado com aids?"


sim_ou_nao(pergunta)
