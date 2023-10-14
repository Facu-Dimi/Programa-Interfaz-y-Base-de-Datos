import tkinter as tk
from client.gui_app import Frame, barra_menu, Login

def main():
    ventana = tk.Tk()
    ventana.title("Netbooks y Pedidos")
    ventana.iconbitmap('Segunda_Interfaz\img\icono.ico')
    ventana.resizable(0,0)
    login = Login(root = ventana)
    #barra_menu(ventana)
    #app = Frame(root = ventana)
    ventana.mainloop()
    

if __name__ == '__main__':
    main()
    
