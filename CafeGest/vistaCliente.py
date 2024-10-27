from Clientes import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conexion import *


class clientes:
    global base
    base = None
    global TexBoxNombre
    TexBoxNombre = None
    global TexBoxApellido
    TexBoxApellido = None
    global groupBox
    groupBox = None
    global tree
    tree = None


def ingresoCliente():
    global TexBoxNombre
    global TexBoxApellido
    global groupBox
    global tree
    global base

    try:
        # Tabla1
        # Crear Ventana
        base = Tk()
        base.geometry("300x150")
        base.title("Formulario Clientes")
        groupBox = LabelFrame(base, text="Datos clientes", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        # Etiquetas

        labelNombre = Label(groupBox, text="Nombre:", width=13, font=("arial", 12)).grid(row=0, column=0)
        TexBoxNombre = Entry(groupBox)
        TexBoxNombre.grid(row=0, column=1)
        labelApellido = Label(groupBox, text="Apellido:", width=13, font=("arial", 12)).grid(row=1, column=0)
        TexBoxApellido = Entry(groupBox)
        TexBoxApellido.grid(row=1, column=1)

        # Botones
        Button(groupBox, text="Guardar", width=10, command=guardar).grid(row=3, column=1)
        base.mainloop()

    except Exception as error:
        print("Error al mostrar la interfaz: {}".format(error))


def guardar():
    global TexBoxNombre, TexBoxApellido, groupBox

    try:
        if TexBoxNombre is None or TexBoxApellido is None:
            print("Los widgets no están inicializados")
            return
        nombre = TexBoxNombre.get()
        apellido = TexBoxApellido.get()

        CClientes.ingresarClientes(nombre, apellido)
        messagebox.showinfo("Información", "Los datos fueron guardados")
        

    except ValueError as error:
        print("Error al ingresar los datos {}".format(error))




    






