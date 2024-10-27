from conexion import *

class CClientes:
    
    
    def mostrarClientes():
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         cursor.execute("select * from usuarios;")
         miResultado = cursor.fetchall()
         cone.commit()
         cone.close()
         return miResultado
            
        except mysql.connector.Error as error:
            print("Error al mostrar datos {}".format(error))
    
    def ingresarClientes(nombre,apellido):
        
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         sql = "insert into usuarios values(null,%s,%s);"
         valores = (nombre,apellido)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Ingresado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            
            
            
    def modificarClientes(idUsuario,nombre,apellido):
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         sql = "UPDATE usuarios SET usuarios.nombre = %s,usuarios.apellido = %sWhere usuarios.id = %s;"
         valores = (nombre,apellido,idUsuario)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Actualizado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error en Actualización de datos {}".format(error))
            

    def eliminarClientes(idUsuario):
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         sql = "DELETE from usuarios WHERE usuarios.id = %s;"
         valores = (idUsuario,)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Eliminado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error en eliminación de datos {}".format(error))