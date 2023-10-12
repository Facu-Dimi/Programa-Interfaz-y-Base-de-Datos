import tkinter as tk
from tkinter import ttk


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    menu_ayuda = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio)
    
    menu_inicio.add_command(label = 'Crear Registro en BD')
    menu_inicio.add_command(label = 'Eliminar Registro de BD')
    menu_inicio.add_command(label = 'Salir', command = root.destroy)
    
    barra_menu.add_cascade(label = 'Consultas')
    barra_menu.add_cascade(label = 'Configuracion')

    barra_menu.add_cascade(label = 'Ayuda', menu = menu_ayuda)

    menu_ayuda.add_command(label = 'Informacion')
    menu_ayuda.add_command(label = 'Reportar Error')







def clicker(num):
    num += 1
    print(num) 


class Frame(tk.Frame):
    
    def __init__(self, root = None):
        super().__init__(root, width = 480, height = 320)
        self.root = root
        self.pack()
        #self.config(bg = 'blue')        
        
        self.campos_pedido()
        self.tabla_datos()
    
    
    def campos_pedido(self):
        
        # Labels[etiquetas] de Cada campo (Columnas de la tabla Pedido):
    
        self.label_numero = tk.Label(self, text = 'Numero de Notebook: ')
        self.label_numero.config(font = ('Arial', 11, 'bold'))
        self.label_numero.grid(row = 0, column = 0, padx = 8, pady = 8)
        
        self.label_alumno = tk.Label(self, text = 'Alumno: ')
        self.label_alumno.config(font = ('Arial', 11, 'bold'))
        self.label_alumno.grid(row = 1, column = 0, padx = 8, pady = 8)
        
        self.label_curso = tk.Label(self, text = 'Curso: ')
        self.label_curso.config(font = ('Arial', 11, 'bold'))
        self.label_curso.grid(row = 2, column = 0, padx = 8, pady = 8)
        
        self.label_profesor = tk.Label(self, text = 'Profesor: ')
        self.label_profesor.config(font = ('Arial', 11, 'bold'))
        self.label_profesor.grid(row = 3, column = 0, padx = 8, pady = 8)
        
        self.label_entrega = tk.Label(self, text = 'Horario de Entrega: ')
        self.label_entrega.config(font = ('Arial', 11, 'bold'))
        self.label_entrega.grid(row = 4, column = 0, padx = 8, pady = 8)
        
        self.label_devolucion = tk.Label(self, text = 'Horario de Devolucion: ')
        self.label_devolucion.config(font = ('Arial', 11, 'bold'))
        self.label_devolucion.grid(row = 5, column = 0, padx = 8, pady = 8)
        
        
        # Entrys[Cuadros de texto] para escribir datos:
        
        self.entry_numero = tk.Entry(self)
        self.entry_numero.config(width = 50, state = 'disabled', font = ('Arial', 11))
        self.entry_numero.grid(row = 0, column = 1, padx = 8, pady = 8)
        
        self.entry_alumno = tk.Entry(self)
        self.entry_alumno.config(width = 50, state = 'disabled', font = ('Arial', 11))
        self.entry_alumno.grid(row = 1, column = 1, padx = 8, pady = 8)
        
        self.entry_curso = tk.Entry(self)
        self.entry_curso.config(width = 50, state = 'disabled', font = ('Arial', 11))
        self.entry_curso.grid(row = 2, column = 1, padx = 8, pady = 8)
        
        self.entry_profesor = tk.Entry(self)
        self.entry_profesor.config(width = 50, state = 'disabled', font = ('Arial', 11))
        self.entry_profesor.grid(row = 3, column = 1, padx = 8, pady = 8)
        
        self.entry_entrega = tk.Entry(self)
        self.entry_entrega.config(width = 50, state = 'disabled', font = ('Arial', 11))
        self.entry_entrega.grid(row = 4, column = 1, padx = 8, pady = 8)
        
        self.entry_devolucion = tk.Entry(self)
        self.entry_devolucion.config(width = 50, state = 'disabled', font = ('Arial', 11))
        self.entry_devolucion.grid(row = 5, column = 1, padx = 8, pady = 8)

        self.entry_busqueda = tk.Entry(self)
        self.entry_busqueda.config(width = 30, state = 'disabled', font = ('Arial', 11))
        self.entry_busqueda.grid(row = 7, column = 0, padx = 10, pady = 10)

        self.entry_muestra = tk.Entry(self)
        self.entry_muestra.config(width = 30, state = 'disabled', font = ('Arial', 11))
        self.entry_muestra.grid(columnspan = 2, row = 7, column = 1, padx = 10, pady = 10)


        
        # Botones
        
        self.boton_registrar = tk.Button(self, text = 'Registrar')
        self.boton_registrar.config(width = 20, font = ('Arial', 11, 'bold'), fg = 'lemon chiffon', bg = 'SteelBlue2',
                                cursor = 'hand2', activebackground = 'SkyBlue1')
        self.boton_registrar.grid(row = 6, column = 0, padx = 10, pady = 10)

        self.boton_limpiar = tk.Button(self, text = 'Limpiar')
        self.boton_limpiar.config(width = 20, font = ('Arial', 11, 'bold'), fg = 'snow', bg = 'dark slate blue',
                                cursor = 'hand2', activebackground = 'slate blue')
        self.boton_limpiar.grid(row = 6, column = 1, padx = 10, pady = 10)

        self.boton_mostrar = tk.Button(self, text = 'Mostrar datos de la base')
        self.boton_mostrar.config(width = 20, font = ('Arial', 11, 'bold'), fg = 'snow', bg = 'midnight blue',
                                cursor = 'hand2', activebackground = 'medium blue')
        self.boton_mostrar.grid(row = 6, column = 2, padx = 10, pady = 10)

        self.boton_buscar = tk.Button(self, text = 'Buscar por Curso')
        self.boton_buscar.config(width = 15, font = ('Arial', 11, 'bold'), fg = 'lemon chiffon', bg = 'SteelBlue2',
                                cursor = 'hand2', activebackground = 'SkyBlue1')
        self.boton_buscar.grid(row = 7, columnspan = 2, column = 0, pady = 10)

        
        self.boton_mostrarfecha = tk.Button(self, text = 'Buscar por Fecha')
        self.boton_mostrarfecha.config(width = 15, font = ('Arial', 11, 'bold'), fg = 'lemon chiffon', bg = 'SteelBlue2',
                                cursor = 'hand2', activebackground = 'SkyBlue1')
        self.boton_mostrarfecha.grid(row = 7, column = 2)

    def tabla_datos(self):
        self.tabla = ttk.Treeview(self, column = ('Alumno', 'Curso', 'Profesor', 'Horario de Entrega', 'Horario de Devolucion'))
        self.tabla.grid(row = 8, column = 0, columnspan = 5)

        self.tabla.heading('#0', text = 'Numero de Netbook')
        self.tabla.heading('#1', text = 'Alumno')
        self.tabla.heading('#2', text = 'Curso')
        self.tabla.heading('#3', text = 'Profesor')
        self.tabla.heading('#4', text = 'Entrega')
        self.tabla.heading('#5', text = 'Devolucion')
    
        self.tabla.insert('', 0, text = '1', 
        values = ('Facu Dimi', '5°1', 'Antonio MitinGAY', '10:23', '16:00'))
        
        