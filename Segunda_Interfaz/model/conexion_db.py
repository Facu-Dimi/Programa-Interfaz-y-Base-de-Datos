import mysql.connector

class Registro_datos():
    
    def __init__(self):
        self.conexion = mysql.connector.connect(host = 'localhost', database = "notebooks", 
                                                user = 'root', password = '123456')
    
    
    def registrar_pedido(self, numero, alumno, curso, profesor, entrega, devolucion):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO pedidos (numero, alumno, curso, profesor, entrega, devolucion)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(numero, alumno, curso, profesor, entrega, devolucion)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
    
    
    def mostrar_pedidos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM pedidos "
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
    
    def editar_pedido(self, numero, alumno, curso, profesor, entrega, devolucion):
        cur = self.conexion.cursor()
        sql = '''UPDATE pedidos
        SET numero = '{}', alumno = '{}', curso = '{}', profesor = '{}', entrega = '{}', devolucion = '{}'
        WHERE id_pedido = '{}'
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
        



