import tkinter as tk

def crear_calculadora():
    def calcular():
        try:
            resultado.set(eval(entrada.get()))
        except:
            resultado.set("Error")

    ventana_calculadora = tk.Toplevel()  # Crear una nueva ventana para la calculadora
    ventana_calculadora.title("Calculadora")
    ventana_calculadora.geometry("300x200")

    resultado = tk.StringVar()  # Variable para almacenar el resultado

    entrada = tk.Entry(ventana_calculadora, font=('Arial', 20))
    entrada.pack(padx=10, pady=10)

    boton_calcular = tk.Button(ventana_calculadora, text="Calcular", command=calcular)
    boton_calcular.pack(padx=10, pady=5)

    etiqueta_resultado = tk.Label(ventana_calculadora, textvariable=resultado, font=('Arial', 20))
    etiqueta_resultado.pack(padx=10, pady=10)
