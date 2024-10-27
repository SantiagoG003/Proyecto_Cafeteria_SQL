import mysql.connector

class Cconexion:
    def conexionBase():
        try:
            conexion = mysql.connector.connect(user = 'root', password = '1006022340',host = '127.0.0.1', database = 'cafeteria',
                                   port = '3306')
            
            print("Conexión correcta")
            return conexion
            
        except mysql.connector.Error as error:
            print("Error al conectarte a la base de Datos {}".format(error))
            
            return conexion
        
    conexionBase()

