import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crudCliente import *
from crudProducto import *
from crudProveedor import *
from calculadora import crear_calculadora
from vistaCliente import ingresoCliente
from carta import listarProductos


def administrador_clicked():
    def mostrar_ventana_login():
        ventana_login = tk.Toplevel(root)
        ventana_login.title("Login de Administrador")
        ventana_login.geometry("300x200")

        # Campos de entrada
        lbl_password = tk.Label(ventana_login, text="Contraseña:")
        lbl_password.pack(pady=5)
        entry_password = tk.Entry(ventana_login, show="*")
        entry_password.pack(pady=5)

        # Función para verificar la contraseña
        def verificar_contraseña():
            if entry_password.get() == "1234":
                ventana_login.destroy()
                mostrar_ventana_administrador()
            else:
                messagebox.showerror("Error", "Contraseña incorrecta")
                ventana_login.destroy()

        # Botón para enviar la contraseña
        btn_login = tk.Button(ventana_login, text="Login", command=verificar_contraseña)
        btn_login.pack(pady=5)

    mostrar_ventana_login()

def mostrar_ventana_administrador():
    ventana_administrador = tk.Toplevel(root)
    ventana_administrador.title("Panel de Administrador")
    ventana_administrador.geometry("400x300")

    # Función para manejar el evento de clic en el botón "Clientes"
    def clientes_clicked():
        FormularioC()
        
    def productos_clicked():
      
        FormularioP()
        
    def proveedores_clicked():
         
        FormularioPr()
       
    def calculadora_clicked():
        
        resultado = crear_calculadora()
        print(resultado)
        
        
    def exit_clicked():
        ventana_administrador.withdraw()   # Oculta la ventana
    
        
    # Crear botones para el panel de administrador
    btn_clientes = tk.Button(ventana_administrador, width=30, height=2, text="Clientes", command=clientes_clicked)
    btn_clientes.pack(pady=10)

    btn_productos = tk.Button(ventana_administrador, width=30, height=2, text="Productos", command=productos_clicked)
    btn_productos.pack(pady=10)

    btn_proveedores = tk.Button(ventana_administrador, width=30, height=2, text="Proveedores", command=proveedores_clicked)
    btn_proveedores.pack(pady=10)
    
    btn_calculadora = tk.Button(ventana_administrador, width=30, height=2, text="Calculadora", command=calculadora_clicked)
    btn_calculadora.pack(pady=10)

    btn_exit = tk.Button(ventana_administrador, width=30, height=2, text="Exit", command=exit_clicked)
    btn_exit.pack(pady=10)

def ventanaCliente():
    ventana_administrador = tk.Toplevel(root)
    ventana_administrador.title("Panel de Cliente")
    ventana_administrador.geometry("400x300")
    
        
    def registro_clicked():  
        ingresoCliente() 
        
    def carta_clicked():
        listarProductos() 
        
    def exitClientes_clicked():
        ventana_administrador.withdraw()
        
         

    btn_clientes = tk.Button(ventana_administrador, width=30, height=2, text="Registrarse", command=registro_clicked)
    btn_clientes.pack(pady=10)

    btn_productos = tk.Button(ventana_administrador, width=30, height=2, text="Carta de productos", command=carta_clicked)
    btn_productos.pack(pady=10)

    btn_exit = tk.Button(ventana_administrador, width=30, height=2, text="Exit", command=exitClientes_clicked)
    btn_exit.pack(pady=10)


    
    
    
def exit_clicked():
    root.destroy()

# Crear ventana principal
root = tk.Tk()
root.title("Bienvenido a CAFEGEST")
root.geometry("400x300")  # Establecer dimensiones de la ventana (ancho x alto)

# Crear botones
btn_administrador = tk.Button(root, width=30 , height=2, text="Administrador", command=administrador_clicked)
btn_administrador.pack(pady=(50, 10))  # Añadir un espacio en la parte superior

btn_clientes = tk.Button(root,  width=30, height=2, text="Clientes", command=ventanaCliente)
btn_clientes.pack(pady=10)

btn_exit = tk.Button(root,  width=30, height=2, text="Exit", command=exit_clicked)
btn_exit.pack(pady=10)

# Ejecutar el bucle principal de la ventana
root.mainloop()






