from conexion import *

class CProveedores:
    
    
    def mostrarProveedores():
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         cursor.execute("select * from proveedores;")
         miResultado = cursor.fetchall()
         cone.commit()
         cone.close()
         return miResultado
            
        except mysql.connector.Error as error:
            print("Error al mostrar datos {}".format(error))
    
    def ingresarProveedores(nombreProveedor,telefono,producto):
        
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         sql = "insert into proveedores values(null,%s,%s,%s);"
         valores = (nombreProveedor,telefono,producto)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Proveedor Ingresado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            
            
            
    def modificarProveedor(idProveedor,nombreProveedor,telefono,producto):
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         sql = "UPDATE proveedores SET proveedores.nombreProveedor = %s,proveedores.telefono = %s,proveedores.producto = %sWhere proveedores.idProveedor = %s;"
         valores = (nombreProveedor,telefono,producto,idProveedor)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Proveedor Actualizado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error en Actualización de datos {}".format(error))
            

    def eliminarProovedor(idProveedor):
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         sql = "DELETE from proveedores WHERE proveedores.idProveedor = %s;"
         valores = (idProveedor,)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Proveedor Eliminado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error en eliminación de datos {}".format(error))