import tkinter as tk
from client.gui_app import Frame, Login

def main():
    ventana = tk.Tk()
    ventana.title("Netbooks y Pedidos")
    ventana.iconbitmap('img\icono.ico')
    ventana.resizable(0,0)
    #login = Login(root = ventana)
    app = Frame(root = ventana)
    ventana.mainloop()
    

if __name__ == '__main__':
    main()
    