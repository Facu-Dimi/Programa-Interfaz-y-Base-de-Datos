import ttkbootstrap as tk
from frames import *

class MainWindow(tk.Window):
    def __init__(self) -> None:
        tk.Window.__init__(self,
                           title= "PyCompu",
                            themename= "darkly",
                            size= (1000,700))
    
        self.crear_frame()
    
    def run(self):
        self.root.mainloop()
    
    def crear_frame(self):
        frame = Frame_Izquierdo(self)
        frame.pack_propagate(False)
        frame2 = Frame_Derecho(self)
        frame.pack(side= "left", padx= 20, pady= 20)
        frame2.pack(side= "left", expand= True, fill= "both", padx= 20, pady= 20)

if __name__ == "__main__":
    ventana = MainWindow()
    ventana.mainloop()
    
#arctic-kiln-401816:southamerica-east1:mi-primera-instancia