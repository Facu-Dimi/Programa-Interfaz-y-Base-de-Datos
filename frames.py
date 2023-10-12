import ttkbootstrap as tk

class Frame_Izquierdo(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self,
                          master= root,
                          borderwidth= 2,
                          relief= "solid",
                          width= 200,
                          height= 300,
                          bootstyle = "primary"
                          )
        
        self.crear_texto()
        
    def crear_texto(self):
        label = tk.Label(self,
                         text= "Ingreso de datos",
                         bootstyle = "inverse-info",
                         font= "Noto-Sans-Telugu 14 bold")
        label.pack(pady= 3)

#############

class Frame_Derecho(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self,
                          master= root,
                          borderwidth= 2,
                          relief= "solid")
        
        self.crear_treeview()

    def crear_treeview(self):
        vista = tk.Treeview(self,
                            columns= ["id", "nombre", "apellido", "curso", "computadora", "tiempo"], show= "headings")
        
        vista.heading("id", text= "ID")
        vista.heading("nombre", text= "Nombre")
        vista.heading("apellido", text= "Apellido")
        vista.heading("curso", text= "Curso")
        vista.heading("computadora", text= "Computadora")
        vista.heading("tiempo", text= "Hora de Entrega")
        
        vista.column("id", width= 20, anchor= "center")
        vista.column("nombre", width= 50, anchor= "center")
        vista.column("apellido", width= 50, anchor= "center")
        vista.column("curso", width= 30, anchor= "center")
        vista.column("computadora", width= 30, anchor= "center")
        vista.column("tiempo", width= 50, anchor= "center")
        
        vista.insert("", "end", values= [0, "javier", "jimenez", "5-1" , "a3", "12:50"])
        
        vista.pack(expand= True, fill= "both")