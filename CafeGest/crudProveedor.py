import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Proveedores import *
from conexion import *


class proveedores:
    global base
    base = None
    global TexBoxIdProveedor
    TexBoxIdProveedor = None
    global TexBoxNombreProveedor
    TexBoxNombreProveedor = None
    global TexBoxTelefono
    TexBoxTelefono = None
    global TexBoxProducto
    TexBoxProducto = None
    global groupBox
    groupBox = None
    global tree
    tree = None


def FormularioPr():
    global TexBoxIdProveedor
    global TexBoxNombreProveedor
    global TexBoxTelefono
    global TexBoxProducto
    global groupBox
    global tree
    global base

    try:
        # Tabla1
        # Crear Ventana
        base = Tk()
        base.geometry("850x500")
        base.title("Formulario Proveedores")
        groupBox = LabelFrame(base, text="Proveedores", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        # Etiquetas
        labelIdProveedor = Label(groupBox, text="Id Proveedor:", width=15, font=("arial", 12)).grid(row=0, column=0)
        TexBoxIdProveedor = Entry(groupBox)
        TexBoxIdProveedor.grid(row=0, column=1)
        labelNombreProveedor = Label(groupBox, text="Nombre Proveedor:", width=15, font=("arial", 12)).grid(row=1, column=0)
        TexBoxNombreProveedor = Entry(groupBox)
        TexBoxNombreProveedor.grid(row=1, column=1)
        labelTelefono = Label(groupBox, text="Telefono proveedor:", width=15, font=("arial", 12)).grid(row=2, column=0)
        TexBoxTelefono = Entry(groupBox)
        TexBoxTelefono.grid(row=2, column=1)
        labelProducto = Label(groupBox, text="Producto:", width=15, font=("arial", 12)).grid(row=3, column=0)
        TexBoxProducto = Entry(groupBox)
        TexBoxProducto.grid(row=3, column=1)

        # Botones
        Button(groupBox, text="Guardar", width=10, command=guardarProveedores).grid(row=4, column=0)
        Button(groupBox, text="Modificar", width=10, command=modificarProveedores).grid(row=4, column=1)
        Button(groupBox, text="Eliminar", width=10, command=eliminarProveedores).grid(row=4, column=2)

        # Tabla 2
        groupBox = LabelFrame(base, text="Lista Proveedores", padx=5, pady=5)
        groupBox.grid(row=3, column=0, padx=5, pady=5)

        # Crear Treeview
        # Configurar columnas
        tree = ttk.Treeview(groupBox, columns=("Id Proveedor", "Nombre Proveedor", "Telefono", "Producto"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Id Proveedor")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Nombre Proveedor")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Telefono")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Producto")


        #Agregar los datos a la tabla
        #Mostrar la tabla
        for row in CProveedores.mostrarProveedores():
            tree.insert("","end",values = row)
            
        #Ejecutar la funcion al hacer clic y mostrar resultado
        tree.bind("<<TreeviewSelect>>",seleccionarProveedores)
        

        tree.pack()

        base.mainloop()

    except Exception as error:
        print("Error al mostrar la interfaz: {}".format(error))

  
  
  
def guardarProveedores():
    global TexBoxNombreProveedor, TexBoxTelefono, TexBoxProducto, groupBox

    try:
        if TexBoxNombreProveedor is None or TexBoxTelefono is None or TexBoxProducto is None:
            print("Los widgets no están inicializados")
            return
        nombreProveedor = TexBoxNombreProveedor.get()
        telefono = TexBoxTelefono.get()
        producto = TexBoxProducto.get()

        CProveedores.ingresarProveedores(nombreProveedor, telefono, producto)
        messagebox.showinfo("Información", "Los datos fueron guardados")
        
        actualizarTreeView()

        # Limpiar datos
        TexBoxNombreProveedor.delete(0, END)
        TexBoxTelefono.delete(0, END)
        TexBoxProducto.delete(0, END)

    except ValueError as error:
        print("Error al ingresar los datos {}".format(error))


def actualizarTreeView():
    global tree
    
    try:
        #Borrar datos actuales del treeView
        tree.delete(*tree.get_children())
        
        #Obtener los datos a 
        #Insertar nuevos datos
        
        for row in CProveedores.mostrarProveedores():
         tree.insert("","end",values = row)
               
    except ValueError as error:
        print("Error al actualizar tabla {}".format(error))

def seleccionarProveedores(event):
    try:
        itemSeleccionado = tree.focus()
        if itemSeleccionado:
            #obtener los valores por columna
            values = tree.item(itemSeleccionado)['values']
            
            #Establecer valores en los widgets
            TexBoxIdProveedor.delete(0, END)
            TexBoxIdProveedor.insert(0,values[0])
            TexBoxNombreProveedor.delete(0, END)
            TexBoxNombreProveedor.insert(0,values[1])
            TexBoxTelefono.delete(0, END)
            TexBoxTelefono.insert(0,values[2])
            TexBoxProducto.delete(0, END)
            TexBoxProducto.insert(0,values[2])
        
        #Obtener id del elemento seleccionado
           
    except ValueError as error:
        print("Error al seleccionar registros {}".format(error))
    


def modificarProveedores():
    global TexBoxIdProveedor,TexBoxNombreProveedor, TexBoxTelefono, TexBoxProducto, groupBox

    try:
        if TexBoxIdProveedor is None or TexBoxNombreProveedor is None or TexBoxTelefono is None or TexBoxProducto is None:
            print("Los widgets no están inicializados")
            return
        idProveedor = TexBoxIdProveedor.get()
        nombreProveedor = TexBoxNombreProveedor.get()
        telefono = TexBoxTelefono.get()
        producto = TexBoxProducto.get()

        CProveedores.modificarProveedor(idProveedor, nombreProveedor, telefono, producto)
        messagebox.showinfo("Información", "Los datos fueron actualizados")
        
        actualizarTreeView()

        # Limpiar datos
        TexBoxIdProveedor.delete(0, END)
        TexBoxNombreProveedor.delete(0, END)
        TexBoxTelefono.delete(0, END)
        TexBoxProducto.delete(0, END)

    except ValueError as error:
        print("Error al actualizar los datos {}".format(error))




#Corregir
def eliminarProveedores():
    global TexBoxIdProveedor,TexBoxNombreProveedor,TexBoxTelefono, TexBoxProducto

    try:
        if TexBoxIdProveedor is None:
            print("Los widgets no están inicializados")
            return
        idProveedor = TexBoxIdProveedor.get()

        CProveedores.eliminarProovedor(idProveedor)
        messagebox.showinfo("Información", "Los datos fueron eliminados")
        
        actualizarTreeView()

        # Limpiar datos
        TexBoxIdProveedor.delete(0, END)
        TexBoxNombreProveedor.delete(0, END)
        TexBoxTelefono.delete(0, END)
        TexBoxProducto.delete(0, END)


    except ValueError as error:
        print("Error al eliminar los datos {}".format(error))



