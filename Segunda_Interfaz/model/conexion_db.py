import mysql.connector

class Registro_datos():
    
    def __init__(self):
        self.conexion = mysql.connector.connect(host = 'localhost', database = "pedidos_notebooks", 
                                                user = 'root', password = '123456')
    
    
    def obtener_curso(self, nombre_alumno):
        cur = self.conexion.cursor()
        sql = '''SELECT curso FROM alumno 
        WHERE Nombre_completo LIKE '{}';'''.format(nombre_alumno)
        cur.execute(sql)
        registro = cur.fetchall()
        return registro
    
    
    def obtener_fecha(self, nro_notebook):
        cur = self.conexion.cursor()
        sql = '''SELECT Fecha, Hora_de_pedido FROM pedido
        WHERE Nro_computadora LIKE '{}';'''.format(nro_notebook)
        cur.execute(sql)
        registro = cur.fetchall()
        return registro
        
    
    
    def registrar_pedido(self, numero, alumno, profesor, entrega):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO pedido (Nro_computadora, alumnoo, profesor, Hora_de_entrega)
        VALUES('{}', '{}', '{}', '{}')'''.format(numero, alumno, profesor, entrega)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
    
    
    def mostrar_pedidos(self):
        cursor = self.conexion.cursor()
        sql = '''SELECT Nro_computadora, Alumnoo, Curso, Profesor, Fecha, Hora_de_pedido, Hora_de_entrega 
        FROM pedido pe
        INNER JOIN alumno al
        ON pe.Alumnoo = al.Nombre_completo;'''
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
    
    
    # Editar y eliminar por el momento no funcionan, tengo que reprogramarlos y adaptarlos a la base de datos de alexis.
    
    def editar_pedido(self, numero, alumno, curso, profesor, entrega, devolucion):
        cur = self.conexion.cursor()
        sql = '''UPDATE pedidos
        SET alumno = '{}', curso = '{}', profesor = '{}', entrega = '{}', devolucion = '{}'
        WHERE numero = '{}'
        '''.format(alumno, curso, profesor, entrega, devolucion, numero)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
    
    def eliminar_pedido(self, numero):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM pedidos where numero = {};'''.format(numero)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
        

