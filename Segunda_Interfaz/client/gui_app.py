import tkinter as tk
from tkinter import ttk, END
from model.conexion_db import *



class Login(tk.Frame):
    
    def __init__(self, root = None):
        super().__init__(root, width = 480, height = 320)
        self.root = root
        self.pack()
        #self.config(bg = 'blue')
        self.clave = 'CuidaLasNetbooks'
        self.clave_ingresada = tk.StringVar()
        self.password()
        
    def password(self):

        self.label_contrasena = tk.Label(self, text = 'Ingrese la contraseña:')
        self.label_contrasena.config(font = ('Arial', 12, 'bold'))
        self.label_contrasena.grid(row = 0, column = 0, padx = 8, pady = 8)
        
        self.entry_contrasena = tk.Entry(self, textvariable = self.clave_ingresada)
        self.entry_contrasena.config(width = 50, font = ('Arial', 11), show = "*")
        self.entry_contrasena.grid(row = 1, column = 0, padx = 8, pady = 8)
        
    
        self.boton_ingresar = tk.Button(self, command = self.comprobar, text = 'Ingresar')
        self.boton_ingresar.config(width = 20, font = ('Arial', 11, 'bold'), fg = 'snow', bg = 'SteelBlue2',
                                cursor = 'hand2', activebackground = 'SkyBlue1')
        self.boton_ingresar.grid(row = 2, column = 0, padx = 10, pady = 10)
        

    def comprobar(self):
        clave_ingresada = self.clave_ingresada.get()
        if clave_ingresada == self.clave:
            self.destroy()
            Frame(self.root)
        else:
            self.entry_contrasena.delete(0, END)
        print(clave_ingresada)



class Frame(tk.Frame):
    
    def __init__(self, root = None):
        super().__init__(root, width = 480, height = 320)
        self.root = root
        self.pack()
        
        self.numero = tk.StringVar()
        self.alumno = tk.StringVar()
        self.curso = tk.StringVar()
        self.profesor = tk.StringVar()
        self.entrega = tk.StringVar()
        self.devolucion = tk.StringVar()
        self.buscar_curso = tk.StringVar()
        self.buscar_fecha = tk.StringVar()
        
        self.base_datos = Registro_datos()
        
        self.barra_menu(root)
        self.campos_pedido()   
        self.tabla_datos()


    def barra_menu(self, root):
        self.barra_menu = tk.Menu(root)
        root.config(menu = self.barra_menu, width = 300, height = 300)
        self.menu_inicio = tk.Menu(self.barra_menu, tearoff = 0)
        self.menu_ayuda = tk.Menu(self.barra_menu, tearoff = 0)
        self.barra_menu.add_cascade(label = 'Inicio', menu = self.menu_inicio)
        self.menu_inicio.add_command(label = 'Crear Registro en BD')
        self.menu_inicio.add_command(label = 'Eliminar Registro de BD')
        self.menu_inicio.add_command(label = 'Salir', command = root.destroy)
        self.barra_menu.add_cascade(label = 'Consultas')
        self.barra_menu.add_cascade(label = 'Configuracion')
        self.barra_menu.add_cascade(label = 'Ayuda', menu = self.menu_ayuda)
        self.menu_ayuda.add_command(label = 'Informacion')
        self.menu_ayuda.add_command(label = 'Reportar Error')
    
    
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
        
        self.entry_numero = tk.Entry(self, textvariable = self.numero)
        self.entry_numero.config(width = 50, font = ('Arial', 11))
        self.entry_numero.grid(row = 0, column = 1, padx = 8, pady = 8)
        
        self.entry_alumno = tk.Entry(self, textvariable = self.alumno)
        self.entry_alumno.config(width = 50, font = ('Arial', 11))
        self.entry_alumno.grid(row = 1, column = 1, padx = 8, pady = 8)
        
        self.entry_curso = tk.Entry(self, textvariable = self.curso)
        self.entry_curso.config(width = 50, font = ('Arial', 11))
        self.entry_curso.grid(row = 2, column = 1, padx = 8, pady = 8)
        
        self.entry_profesor = tk.Entry(self, textvariable = self.profesor)
        self.entry_profesor.config(width = 50, font = ('Arial', 11))
        self.entry_profesor.grid(row = 3, column = 1, padx = 8, pady = 8)
        
        self.entry_entrega = tk.Entry(self, textvariable = self.entrega)
        self.entry_entrega.config(width = 50, font = ('Arial', 11))
        self.entry_entrega.grid(row = 4, column = 1, padx = 8, pady = 8)
        
        self.entry_devolucion = tk.Entry(self, textvariable = self.devolucion)
        self.entry_devolucion.config(width = 50, font = ('Arial', 11))
        self.entry_devolucion.grid(row = 5, column = 1, padx = 8, pady = 8)

        self.entry_busqueda = tk.Entry(self)
        self.entry_busqueda.config(width = 30, font = ('Arial', 11))
        self.entry_busqueda.grid(row = 7, column = 0, padx = 10, pady = 10)

        self.entry_muestra = tk.Entry(self)
        self.entry_muestra.config(width = 30, font = ('Arial', 11))
        self.entry_muestra.grid(columnspan = 2, row = 7, column = 1, padx = 10, pady = 10)


        
        # Botones
        
        self.boton_registrar = tk.Button(self, command = self.registrar_datos, text = 'Registrar')
        self.boton_registrar.config(width = 20, font = ('Arial', 11, 'bold'), fg = 'snow', bg = 'SteelBlue2',
                                cursor = 'hand2', activebackground = 'SkyBlue1')
        self.boton_registrar.grid(row = 6, column = 0, padx = 10, pady = 10)

        self.boton_limpiar = tk.Button(self, command = self.limpiar_datos, text = 'Limpiar')
        self.boton_limpiar.config(width = 20, font = ('Arial', 11, 'bold'), fg = 'snow', bg = 'dark slate blue',
                                cursor = 'hand2', activebackground = 'slate blue')
        self.boton_limpiar.grid(row = 6, column = 1, padx = 10, pady = 10)

        self.boton_mostrar = tk.Button(self, command = self.mostrar_datos, text = 'Mostrar datos de la base')
        self.boton_mostrar.config(width = 20, font = ('Arial', 11, 'bold'), fg = 'snow', bg = 'midnight blue',
                                cursor = 'hand2', activebackground = 'medium blue')
        self.boton_mostrar.grid(row = 6, column = 2, padx = 10, pady = 10)

        self.boton_buscar = tk.Button(self, text = 'Buscar por Curso')
        self.boton_buscar.config(width = 15, font = ('Arial', 11, 'bold'), fg = 'snow', bg = 'CadetBlue3',
                                cursor = 'hand2', activebackground = 'CadetBlue1')
        self.boton_buscar.grid(row = 7, columnspan = 2, column = 0, pady = 10)

        self.boton_mostrarfecha = tk.Button(self, text = 'Buscar por Fecha')
        self.boton_mostrarfecha.config(width = 15, font = ('Arial', 11, 'bold'), fg = 'snow', bg = 'aquamarine3',
                                cursor = 'hand2', activebackground = 'aquamarine')
        self.boton_mostrarfecha.grid(row = 7, column = 2)
        
        self.boton_modificar = tk.Button(self, command = self.modificar_datos, text = 'Modificar')
        self.boton_modificar.config(width = 20, font = ('Arial', 11, 'bold'), fg = 'snow', bg = 'dark slate blue',
                                cursor = 'hand2', activebackground = 'slate blue')
        self.boton_modificar.grid(row = 9, column = 0, padx = 10, pady = 10)
        
        self.boton_eliminar = tk.Button(self, command= self.eliminar_datos, text = 'Eliminar')
        self.boton_eliminar.config(width = 20, font = ('Arial', 11, 'bold'), fg = 'snow', bg = 'dark slate blue',
                                cursor = 'hand2', activebackground = 'slate blue')
        self.boton_eliminar.grid(row = 9, columnspan = 2, column = 0, padx = 10, pady = 10)

    
    def limpiar_campos(self):
        self.numero.set('')
        self.alumno.set('')
        self.curso.set('')
        self.profesor.set('')
        self.entrega.set('')
        self.devolucion.set('')
    
    
    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        self.limpiar_campos()
    


    def tabla_datos(self):
        self.tabla = ttk.Treeview(self, column = ('Alumno', 'Curso', 'Profesor', 'Horario de Entrega', 'Horario de Devolucion'))
        self.tabla.grid(row = 8, column = 0, columnspan = 5, sticky= 'nse')
        
        self.scroll = ttk.Scrollbar(self, orient = 'vertical', command = self.tabla.yview)
        self.scroll.grid(row = 8, column = 5, sticky = 'nse')
        self.tabla.configure(yscrollcommand = self.scroll.set)

        self.tabla.heading('#0', text = 'Numero de Netbook')
        self.tabla.heading('#1', text = 'Alumno')
        self.tabla.heading('#2', text = 'Curso')
        self.tabla.heading('#3', text = 'Profesor')
        self.tabla.heading('#4', text = 'Entrega')
        self.tabla.heading('#5', text = 'Devolucion')
        
    


    def registrar_datos(self):
        self.tabla.get_children()
        numero = self.numero.get()
        alumno = self.alumno.get()
        curso = self.curso.get()
        profesor = self.profesor.get()
        entrega = self.entrega.get()
        devolucion = self.devolucion.get()
        datos = (alumno, curso, profesor, entrega, devolucion)
        if numero and alumno and curso and profesor and entrega and devolucion !='':
            try:        
                self.tabla.insert('',0, text = numero, values=datos)
                self.base_datos.registrar_pedido(numero, alumno, curso, profesor, entrega, devolucion)
            except:
                self.limpiar_campos()
        self.limpiar_campos()
        

    def mostrar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_pedidos()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert('',i, text = registro[i][1:2], values=registro[i][2:7])
    
    
    def modificar_datos(self):
        self.numero = self.tabla.item(self.tabla.selection())['text']
        self.alumno = self.tabla.item(self.tabla.selection())['values'][0]
        self.curso = self.tabla.item(self.tabla.selection())['values'][1]
        self.profesor = self.tabla.item(self.tabla.selection())['values'][2]
        self.entrega = self.tabla.item(self.tabla.selection())['values'][3]
        self.devolucion = self.tabla.item(self.tabla.selection())['values'][4]
            
        self.entry_numero.insert(0, self.numero)
        self.entry_alumno.insert(0, self.alumno)
        self.entry_curso.insert(0, self.curso)
        self.entry_profesor.insert(0, self.profesor)
        self.entry_entrega.insert(0, self.entrega)
        self.entry_devolucion.insert(0, self.devolucion)
    
    
    def eliminar_datos(self):
        fila = self.tabla.selection()
        numero = (self.tabla.item(self.tabla.selection()))['text']
        self.base_datos.eliminar_pedido(numero)
        self.tabla.delete(fila)
        
    
    
    


        