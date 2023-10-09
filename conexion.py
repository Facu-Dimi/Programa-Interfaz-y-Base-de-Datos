import mysql.connector

class Registro_datos():
    
    def __init__(self):
        self.conexion = mysql.connector.connect(host = 'localhost', database = "el_virgilio", 
                                                user = 'root', password = '123456')
    
    def insertar_cultivador(self, dni, hectareadesignada, nombrecompleto, direccion, salario, contacto):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO cultivadores (DNI, HectareaDesignada, nombreCompleto, direccion, contacto)
        VALUES('{}', '{}', '{}', '{}', '{}')'''.format(dni, hectareadesignada, nombrecompleto, direccion, salario, contacto)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
    
    
    def mostrar_cultivadores(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM cultivadores "
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro



datos = Registro_datos()