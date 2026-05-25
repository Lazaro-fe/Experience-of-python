import customtkinter as ctk 
import os
import webbrowser

# FUNÇÕES

def tela():
    janela2 = ctk.CTkToplevel()
    janela2.attributes("-fullscreen", True)
    janela2.configure(fg_color="#0078D7")
    mensagem = """
    
    : (
        
        SE FUDEU SEU ALUNO
    """
    
    texto = ctk.CTkLabel(janela2,
                             text=mensagem,
                             font=('roboto', 40),
                             text_color='white')
    texto.pack(expand=True)
    

def desligar():
    os.system('shutdown /s /t 0')
def reiniciar():
    os.system('shutdown /r /t 0')
def google():
    webbrowser.open('https://www.google.com/search?newwindow=1&sca_esv=fc0429090c82337a&sxsrf=ANbL-n5LJc0QPwH2LyKvZtiyPg2ta82--A:1779731010813&udm=2&fbs=ADc_l-acAb_3MMOAUx0zmbUpgBqRiigBgL2I_pgQa-94zvB054Dys3s2x_Qm_GJcU2DlSXieuCxH018RGsE0xvw2_HKhudJGWgXPA5hzXkv3QZ3bycnrH81YaDJc-ckKqEMoXWJXeBypyONrUrKEm3DJMjWageVO6VuKPIkd09xJdUXmYGQLeFFw-OwM8agjQkdhWI9sJDUV7XdHQmUFaKLrJSmUVAgQKg&q=macaco+babu%C3%ADno&sa=X&ved=2ahUKEwi8ysfV_tSUAxU0qpUCHR84H4oQtKgLegQIXRAB&biw=1080&bih=1785&dpr=1')
def block():
    os.system('rundll32.exe user32.dll,LockWorkStation')
def calculadora():
    os.system('calc')
def surpresa():
    webbrowser.open('https://spinning.fish/')

# JANELA PRINCIPAL
janela = ctk.CTk()
janela.geometry("300x500")
janela.resizable(False, False)
janela.title("BOMBA-PACTH 2026")

# INICIO DE JANELA
titulo = ctk.CTkLabel(janela,
                     text= "Bomba Pacth 2026",
                     font=("Roboto", 30, "bold"),
                     text_color="Black")
titulo.pack(pady = 10)

bt01 = ctk.CTkButton(janela,
                    width=200,
                    height=30,
                    fg_color='black',
                    text_color='white',
                    text='Desligar',
                    font=('Roboto', 30),
                    command=desligar)
bt01.pack(pady=10)


bt02 = ctk.CTkButton(janela,
                    width=200,
                    height=30,
                    fg_color='black',
                    text_color='white',
                    text='Reiniciar',
                    font=('Roboto', 30),
                    command=reiniciar)
bt02.pack(pady=10)



bt03 = ctk.CTkButton(janela,
                    width=215,
                    height=30,
                    fg_color='black',
                    text_color='white',
                    text='Bloquear',
                    font=('Roboto', 30),
                    command= block)
bt03.pack()



bt04 = ctk.CTkButton(janela,
                    width=215,
                    height=30,
                    fg_color='black',
                    text_color='white',
                    text='Calculadora',
                    font=('Roboto', 30),
                    command=calculadora)
bt04.pack(pady=10)



bt05 = ctk.CTkButton(janela,
                    width=215,
                    height=30,
                    fg_color='black',
                    text_color='white',
                    text='Google',
                    font=('Roboto', 30),
                    command = google)
bt05.pack()



bt06 = ctk.CTkButton(janela,
                    width=215,
                    height=30,
                    fg_color='black',
                    text_color='white',
                    text='Surpresa',
                    font=('Roboto', 30),
                    command=surpresa)
bt06.pack(pady=10)

bt07 = ctk.CTkButton(janela,
                    width=215,
                    height=30,
                    fg_color='black',
                    text_color='white',
                    text='TELA 2',
                    font=('Roboto', 30),
                    command=tela)
bt07.pack(pady=10)


janela.mainloop()