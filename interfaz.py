import tkinter as tk  
from tkinter import ttk
import json

with open('errores.json', 'r') as file:
    data = json.load(file)

def obtenerValor():
    entrada = entrada_texto.get()
    print(entrada)
    for error in data['errores']:
        if error['error'] == entrada:
            print("Error encontrado")

#crear la ventana
ventana = tk.Tk()
ventana.title("Busqueda de error")

titulo = ttk.Label(ventana, text="Ingresa el codigo", font="Calibri 24")
titulo.pack(padx=10, pady=10)

entrada_texto = ttk.Entry(ventana)
entrada_texto.pack(padx=10, pady=10)

btn_buscar = ttk.Button(ventana, text="Buscar codigo", command=obtenerValor)
btn_buscar.pack(padx=10, pady=10)

descripcion = ttk.Label(ventana,text="")
descripcion.pack(padx=10, pady=10)

ventana.mainloop() #va al final
