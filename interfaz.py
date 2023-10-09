from tkinter import Entry, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END
from conexion import *

base_datos = Registro_datos()

class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
                                    
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0,row=0)
        self.frame2 = Frame(master, bg='navy')
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(master, bg='black')
        self.frame4.grid(column=0, row=2)

        self.dni = StringVar()
        self.hectareadesignada = StringVar()
        self.nombrecompleto = StringVar()
        self.direccion = StringVar()
        self.salario = StringVar()
        self.contacto = StringVar()

        self.base_datos = Registro_datos()
        self.create_wietgs()

    def create_wietgs(self):
        Label(self.frame1, text = 'R E G I S T R O \t D E \t D A T O S',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        Label(self.frame2, text = 'Agregar Nuevos Datos',fg='white', bg ='navy', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame2, text = 'DNI',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame2, text = 'Hectarea Designada',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame2, text = 'Nombre Completo',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame2, text = 'Direccion', fg='white',bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame2, text = 'Salario',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
        Label(self.frame2, text = 'Contacto',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15)


        Entry(self.frame2,textvariable=self.dni , font=('Arial',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame2,textvariable=self.hectareadesignanda , font=('Arial',12)).grid(column=1,row=2)
        Entry(self.frame2,textvariable=self.nombrecompleto , font=('Arial',12)).grid(column=1,row=3)
        Entry(self.frame2,textvariable=self.direccion , font=('Arial',12)).grid(column=1,row=4)
        Entry(self.frame2,textvariable=self.salario , font=('Arial',12)).grid(column=1,row=5)
        Entry(self.frame2,textvariable=self.contacto , font=('Arial',12)).grid(column=1,row=6)
       
        Label(self.frame4, text = 'Control',fg='white', bg ='black', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)         
        Button(self.frame4,command= self.agregar_datos, text='REGISTRAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=0,row=1, pady=10, padx=4)
        #Button(self.frame4,command = self.limpiar_datos, text='LIMPIAR', font=('Arial',10,'bold'), bg='orange red').grid(column=1,row=1, padx=10)        
        #Button(self.frame4,command = self.eliminar_fila, text='ELIMINAR', font=('Arial',10,'bold'), bg='yellow').grid(column=2,row=1, padx=4)
        #Button(self.frame4,command = self.buscar_nombre, text='BUSCAR POR NOMBRE', font=('Arial',8,'bold'), bg='orange').grid(columnspan=2,column = 1, row=2)
        #Entry(self.frame4,textvariable=self.buscar , font=('Arial',12), width=10).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame4,command = self.mostrar_todo, text='MOSTRAR DATOS DE MYSQL', font=('Arial',10,'bold'), bg='green2').grid(columnspan=3,column=0,row=3, pady=8)


        self.tabla = ttk.Treeview(self.frame3, height=21)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.frame3, orient =VERTICAL, command = self.tabla.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        self.tabla['columns'] = ('dni', 'hectareadesignada', 'nombrecompleto', 'direccion', 'salario', 'contacto')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('HectareaDesignada', minwidth=100, width=130 , anchor='center')
        self.tabla.column('NombreCompleto', minwidth=100, width=120, anchor='center' )
        self.tabla.column('Direccion', minwidth=100, width=120 , anchor='center')
        self.tabla.column('Salario', minwidth=100, width=105, anchor='center')
        self.tabla.column('Contacto', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text='DNI', anchor ='center')
        self.tabla.heading('HectareaDesignada', text='HectareaDesignada', anchor ='center')
        self.tabla.heading('NombreCompleto', text='NombreCompleto', anchor ='center')
        self.tabla.heading('Direccion', text='Direccion', anchor ='center')
        self.tabla.heading('Salario', text='Salario', anchor ='center')
        self.tabla.heading('Contacto', text='Contacto', anchor ='center')


        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila
        

    def agregar_datos(self):
        self.tabla.get_children()
        dni = self.codigo.get() 
        hectareadesignada = self.codigo.get() 
        nombrecompleto = self.codigo.get() 
        direccion = self.codigo.get()
        salario = self.codigo.get() 
        contacto = self.codigo.get()
        datos = (dni, hectareadesignada, nombrecompleto, direccion, salario, contacto)
        if dni and hectareadesignada and nombrecompleto and direccion and salario and contacto !='':        
            self.tabla.insert('',0, text = dni, values=datos)
            self.base_datos.insertar_cultivador(dni, hectareadesignada, nombrecompleto, direccion, salario, contacto)


    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        self.dni.set('')
        self.hectareadesignada.set('')
        self.nombrecompleto.set('')
        self.direccion.set('')
        self.salario.set('')
        self.contacto.set('')
    
    '''
    def buscar_nombre(self):
        nombre_producto = self.buscar.get()
        nombre_producto = str("'" + nombre_producto + "'")
        nombre_buscado = self.base_datos.busca_producto(nombre_producto)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla.insert('',i, text = nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])
    '''

    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_cultivadores()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert('',i, text = registro[i][1:2], values=registro[i][2:6])
    
    '''
    def eliminar_fila(self):
        fila = self.tabla.selection()
        if len(fila) !=0:        
            self.tabla.delete(fila)
            nombre = ("'"+ str(self.nombre_borar) + "'")       
            self.base_datos.elimina_productos(nombre)
            
    
    
    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]
    '''
   

def main():
    ventana = Tk()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('900x500')
    ventana.resizable(0,0)
    app = Registro(ventana)
    app.mainloop()

if __name__=="__main__":
    main()        








'''
ventana = tkinter.Tk()
ventana.geometry("500x500")

DNI = StringVar()
HectareaDesignada = StringVar()
nombreCompleto = StringVar()
direccion = StringVar()
salario = StringVar()
contacto = StringVar()

etiqueta = tkinter.Label(ventana, text = "Putos Ngeros", bg = "pink")
etiqueta.pack(fill = tkinter.X)

boton1 = tkinter.Button(ventana, text = "Tikitiki ala pantaya", font=('Comic Sans MS',14,'italic'), bg = "snow")
boton1.pack()

ventana.mainloop()