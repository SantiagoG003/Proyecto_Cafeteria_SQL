from conexion import *

class CProductos:
    
    
    def mostrarProductos():
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         cursor.execute("select * from productos;")
         miResultado = cursor.fetchall()
         cone.commit()
         cone.close()
         return miResultado
            
        except mysql.connector.Error as error:
            print("Error al mostrar datos {}".format(error))
    
    def ingresarProductos(nombreProducto,precioUnitario,disponibilidad):
        
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         sql = "insert into productos values(null,%s,%s,%s);"
         valores = (nombreProducto,precioUnitario,disponibilidad)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Producto Ingresado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            
            
            
    def modificarProducto(idProducto,nombreProducto,precioUnitario,disponibilidad):
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         sql = "UPDATE productos SET productos.nombreProducto = %s,productos.precioUnitario = %s,productos.disponibilidad = %sWhere productos.idProducto = %s;"
         valores = (nombreProducto,precioUnitario,disponibilidad,idProducto)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Producto Actualizado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error en Actualización de datos {}".format(error))
            

    def eliminarProductos(idProducto):
        try:
         cone = Cconexion.conexionBase()
         cursor = cone.cursor()
         sql = "DELETE from productos WHERE productos.idProducto = %s;"
         valores = (idProducto,)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Producto Eliminado")
         cone.close()
            
        except mysql.connector.Error as error:
            print("Error en eliminación de datos {}".format(error))