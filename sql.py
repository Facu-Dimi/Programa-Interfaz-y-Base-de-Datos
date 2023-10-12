import pymysql as sql

def conectar():
    try:
        connect = sql.connect(host= "34.151.228.130",
                        user= "root",
                        passwd= "",
                        database= "proyecto",
                        charset= "utf8mb4",
                        cursorclass= sql.cursors.DictCursor)
    except:
        print("xd")
        return None

    return connect


def consultar():
    
    connect = conectar()
       
    with connect:
        with connect.cursor() as cursor:
            algo = "select * from alumno"
            cursor.execute(algo)
            result = cursor.fetchall()
            
            print(result)
        
#### ejemplo de como insertar

def insertar():
    
    connect = conectar()
    
    with connect:
        with connect.cursor() as cursor:
            algo = "insert into alumno(nombre, apellido, curso, computadora) values ('Agustin', 'Jerez', '5-1', 'A33');"
            cursor.execute(algo)
        
        connect.commit()

print(consultar())