import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Clientes import *
from conexion import *


class clientes:
    global base
    base = None
    global TexBoxId
    TexBoxId = None
    global TexBoxNombre
    TexBoxNombre = None
    global TexBoxApellido
    TexBoxApellido = None
    global groupBox
    groupBox = None
    global tree
    tree = None


def FormularioC():
    global TexBoxId
    global TexBoxNombre
    global TexBoxApellido
    global groupBox
    global tree
    global base

    try:
        # Tabla1
        # Crear Ventana
        base = Tk()
        base.geometry("650x500")
        base.title("Formulario Clientes")
        groupBox = LabelFrame(base, text="Datos clientes", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        # Etiquetas
        labelId = Label(groupBox, text="Id Cliente:", width=13, font=("arial", 12)).grid(row=0, column=0)
        TexBoxId = Entry(groupBox)
        TexBoxId.grid(row=0, column=1)
        labelNombre = Label(groupBox, text="Nombre:", width=13, font=("arial", 12)).grid(row=1, column=0)
        TexBoxNombre = Entry(groupBox)
        TexBoxNombre.grid(row=1, column=1)
        labelApellido = Label(groupBox, text="Apellido:", width=13, font=("arial", 12)).grid(row=2, column=0)
        TexBoxApellido = Entry(groupBox)
        TexBoxApellido.grid(row=2, column=1)

        # Botones
        Button(groupBox, text="Guardar", width=10, command=guardarRegistros).grid(row=3, column=0)
        Button(groupBox, text="Modificar", width=10, command=modificarRegistros).grid(row=3, column=1)
        Button(groupBox, text="Eliminar", width=10, command=eliminarRegistros ).grid(row=3, column=2)

        # Tabla 2
        groupBox = LabelFrame(base, text="Lista Clientes", padx=5, pady=5)
        groupBox.grid(row=3, column=0, padx=5, pady=5)

        # Crear Treeview
        # Configurar columnas
        tree = ttk.Treeview(groupBox, columns=("Id Cliente", "Nombre", "Apellido"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Id Cliente")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Nombre")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Apellido")


        #Agregar los datos a la tabla
        #Mostrar la tabla
        for row in CClientes.mostrarClientes():
            tree.insert("","end",values = row)
            
        #Ejecutar la funcion al hacer clic y mostrar resultado
        tree.bind("<<TreeviewSelect>>",seleccionarRegistro)
        

        tree.pack()

        base.mainloop()

    except Exception as error:
        print("Error al mostrar la interfaz: {}".format(error))


def guardarRegistros():
    global TexBoxNombre, TexBoxApellido, groupBox

    try:
        if TexBoxNombre is None or TexBoxApellido is None:
            print("Los widgets no están inicializados")
            return
        nombre = TexBoxNombre.get()
        apellido = TexBoxApellido.get()

        CClientes.ingresarClientes(nombre, apellido)
        messagebox.showinfo("Información", "Los datos fueron guardados")
        
        actualizarTreeView()

        # Limpiar datos
        TexBoxNombre.delete(0, END)
        TexBoxApellido.delete(0, END)

    except ValueError as error:
        print("Error al ingresar los datos {}".format(error))


def actualizarTreeView():
    global tree
    
    try:
        #Borrar datos actuales del treeView
        tree.delete(*tree.get_children())
        
        #Obtener los datos a 
        #Insertar nuevos datos
        
        for row in CClientes.mostrarClientes():
         tree.insert("","end",values = row)
               
    except ValueError as error:
        print("Error al actualizar tabla {}".format(error))

def seleccionarRegistro(event):
    try:
        itemSeleccionado = tree.focus()
        if itemSeleccionado:
            #obtener los valores por columna
            values = tree.item(itemSeleccionado)['values']
            
            #Establecer valores en los widgets
            TexBoxId.delete(0, END)
            TexBoxId.insert(0,values[0])
            TexBoxNombre.delete(0, END)
            TexBoxNombre.insert(0,values[1])
            TexBoxApellido.delete(0, END)
            TexBoxApellido.insert(0,values[2])
        
        #Obtener id del elemento seleccionado
           
    except ValueError as error:
        print("Error al seleccionar registros {}".format(error))
    


def modificarRegistros():
    global TexBoxId,TexBoxNombre, TexBoxApellido, groupBox

    try:
        if TexBoxId is None or TexBoxNombre is None or TexBoxApellido is None:
            print("Los widgets no están inicializados")
            return
        idUsuario = TexBoxId.get()
        nombre = TexBoxNombre.get()
        apellido = TexBoxApellido.get()

        CClientes.modificarClientes(idUsuario,nombre, apellido)
        messagebox.showinfo("Información", "Los datos fueron actualizados")
        
        actualizarTreeView()

        # Limpiar datos
        TexBoxId.delete(0, END)
        TexBoxNombre.delete(0, END)
        TexBoxApellido.delete(0, END)

    except ValueError as error:
        print("Error al actualizar los datos {}".format(error))



def eliminarRegistros():
    global TexBoxId,TexBoxNombre,TexBoxApellido

    try:
        if TexBoxId is None:
            print("Los widgets no están inicializados")
            return
        idUsuario = TexBoxId.get()

        CClientes.eliminarClientes(idUsuario)
        messagebox.showinfo("Información", "Los datos fueron eliminados")
        
        actualizarTreeView()

        # Limpiar datos
        TexBoxId.delete(0, END)
        TexBoxNombre.delete(0, END)
        TexBoxApellido.delete(0, END)


    except ValueError as error:
        print("Error al eliminar los datos {}".format(error))










