import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Productos import *
from conexion import *


class productos:
    global base
    base = None
    global TexBoxIdProducto
    TexBoxIdProducto = None
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


def FormularioP():
    global TexBoxIdProducto
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
        base.geometry("850x500")
        base.title("Formulario Productos")
        groupBox = LabelFrame(base, text="Productos", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        # Etiquetas
        labelIdProducto = Label(groupBox, text="Id Producto:", width=15, font=("arial", 12)).grid(row=0, column=0)
        TexBoxIdProducto = Entry(groupBox)
        TexBoxIdProducto.grid(row=0, column=1)
        labelNombreProducto = Label(groupBox, text="Nombre Producto:", width=15, font=("arial", 12)).grid(row=1, column=0)
        TexBoxNombreProducto = Entry(groupBox)
        TexBoxNombreProducto.grid(row=1, column=1)
        labelPrecioUnitario = Label(groupBox, text="Precio Unitario:", width=15, font=("arial", 12)).grid(row=2, column=0)
        TexBoxPrecioUnitario = Entry(groupBox)
        TexBoxPrecioUnitario.grid(row=2, column=1)
        labelDisponibilidad = Label(groupBox, text="Disponibilidad:", width=15, font=("arial", 12)).grid(row=3, column=0)
        TexBoxDisponibilidad = Entry(groupBox)
        TexBoxDisponibilidad.grid(row=3, column=1)

        # Botones
        Button(groupBox, text="Guardar", width=10, command=guardarProductos).grid(row=4, column=0)
        Button(groupBox, text="Modificar", width=10, command=modificarProductos).grid(row=4, column=1)
        Button(groupBox, text="Eliminar", width=10, command=eliminarProductos).grid(row=4, column=2)

        # Tabla 2
        groupBox = LabelFrame(base, text="Lista Productos", padx=5, pady=5)
        groupBox.grid(row=3, column=0, padx=5, pady=5)

        # Crear Treeview
        # Configurar columnas
        tree = ttk.Treeview(groupBox, columns=("Id Producto", "Nombre Producto", "Precio Unitario", "Disponibilidad"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Id Producto")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Nombre Producto")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Precio Unitario")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Disponibilidad")


        #Agregar los datos a la tabla
        #Mostrar la tabla
        for row in CProductos.mostrarProductos():
            tree.insert("","end",values = row)
            
        #Ejecutar la funcion al hacer clic y mostrar resultado
        tree.bind("<<TreeviewSelect>>",seleccionarProductos)
        

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

def seleccionarProductos(event):
    try:
        itemSeleccionado = tree.focus()
        if itemSeleccionado:
            #obtener los valores por columna
            values = tree.item(itemSeleccionado)['values']
            
            #Establecer valores en los widgets
            TexBoxIdProducto.delete(0, END)
            TexBoxIdProducto.insert(0,values[0])
            TexBoxNombreProducto.delete(0, END)
            TexBoxNombreProducto.insert(0,values[1])
            TexBoxPrecioUnitario.delete(0, END)
            TexBoxPrecioUnitario.insert(0,values[2])
            TexBoxDisponibilidad.delete(0, END)
            TexBoxDisponibilidad.insert(0,values[2])
        
        #Obtener id del elemento seleccionado
           
    except ValueError as error:
        print("Error al seleccionar registros {}".format(error))
    


def modificarProductos():
    global TexBoxIdProducto,TexBoxNombreProducto, TexBoxPrecioUnitario, TexBoxDisponibilidad, groupBox

    try:
        if TexBoxIdProducto is None or TexBoxNombreProducto is None or TexBoxPrecioUnitario is None or TexBoxDisponibilidad is None:
            print("Los widgets no están inicializados")
            return
        idProducto = TexBoxIdProducto.get()
        nombreProducto = TexBoxNombreProducto.get()
        precioUnitario = TexBoxPrecioUnitario.get()
        disponibilidad = TexBoxDisponibilidad.get()

        CProductos.modificarProducto(idProducto, nombreProducto, precioUnitario, disponibilidad)
        messagebox.showinfo("Información", "Los datos fueron actualizados")
        
        actualizarTreeView()

        # Limpiar datos
        TexBoxIdProducto.delete(0, END)
        TexBoxNombreProducto.delete(0, END)
        TexBoxPrecioUnitario.delete(0, END)
        TexBoxDisponibilidad.delete(0, END)

    except ValueError as error:
        print("Error al actualizar los datos {}".format(error))



def eliminarProductos():
    global TexBoxIdProducto,TexBoxNombreProducto,TexBoxPrecioUnitario, TexBoxDisponibilidad

    try:
        if TexBoxIdProducto is None:
            print("Los widgets no están inicializados")
            return
        idProducto = TexBoxIdProducto.get()

        CProductos.eliminarProductos(idProducto)
        messagebox.showinfo("Información", "Los datos fueron eliminados")
        
        actualizarTreeView()

        # Limpiar datos
        TexBoxIdProducto.delete(0, END)
        TexBoxNombreProducto.delete(0, END)
        TexBoxPrecioUnitario.delete(0, END)
        TexBoxDisponibilidad.delete(0, END)


    except ValueError as error:
        print("Error al eliminar los datos {}".format(error))





