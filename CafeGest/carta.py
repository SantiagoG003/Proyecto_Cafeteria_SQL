import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Productos import *
from conexion import *


class productos:
    global base
    base = None
    global TexBoxNombreProducto
    TexBoxNombreProducto = None
    global TexBoxPrecioUnitario
    TexBoxPrecioUnitario = None
    global TexBoxDisponibilidad
    TexBoxDisponibilidad = None
    global groupBox
    groupBox = None
    global tree
    tree = None


def listarProductos():
    global TexBoxNombreProducto
    global TexBoxPrecioUnitario
    global TexBoxDisponibilidad
    global groupBox
    global tree
    global base

    try:
        # Tabla1
        # Crear Ventana
        base = Tk()
        base.geometry("650x400")
        base.title("Formulario Productos")
        groupBox = LabelFrame(base, text="Productos", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)


        # Tabla 
        groupBox = LabelFrame(base, text="Lista Productos", padx=5, pady=5)
        groupBox.grid(row=3, column=0, padx=5, pady=5)

        # Crear Treeview
        # Configurar columnas
        tree = ttk.Treeview(groupBox, columns=("Nombre Producto", "Precio Unitario", "Disponibilidad"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Id Producto")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Nombre Producto")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Precio Unitario")


        #Agregar los datos a la tabla
        #Mostrar la tabla
        for row in CProductos.mostrarProductos():
            tree.insert("","end",values = row)
            
        #Ejecutar la funcion al hacer clic y mostrar resultado
        #tree.bind("<<TreeviewSelect>>",seleccionarProductos)
        

        tree.pack()

        base.mainloop()

    except Exception as error:
        print("Error al mostrar la interfaz: {}".format(error))

  
  
  
def guardarProductos():
    global TexBoxNombreProducto, TexBoxPrecioUnitario, TexBoxDisponibilidad, groupBox

    try:
        if TexBoxNombreProducto is None or TexBoxPrecioUnitario is None or TexBoxDisponibilidad is None:
            print("Los widgets no están inicializados")
            return
        nombreProducto = TexBoxNombreProducto.get()
        precioUnitario = TexBoxPrecioUnitario.get()
        disponibilidad = TexBoxDisponibilidad.get()

        CProductos.ingresarProductos(nombreProducto, precioUnitario, disponibilidad)
        messagebox.showinfo("Información", "Los datos fueron guardados")
        
        actualizarTreeView()

        # Limpiar datos
        TexBoxNombreProducto.delete(0, END)
        TexBoxPrecioUnitario.delete(0, END)
        TexBoxDisponibilidad.delete(0, END)

    except ValueError as error:
        print("Error al ingresar los datos {}".format(error))


def actualizarTreeView():
    global tree
    
    try:
        #Borrar datos actuales del treeView
        tree.delete(*tree.get_children())
        
        #Obtener los datos a 
        #Insertar nuevos datos
        
        for row in CProductos.mostrarProductos():
         tree.insert("","end",values = row)
               
    except ValueError as error:
        print("Error al actualizar tabla {}".format(error))








