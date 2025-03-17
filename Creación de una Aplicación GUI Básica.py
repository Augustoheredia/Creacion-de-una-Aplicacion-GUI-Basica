import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entry.get().strip()  # Obtener el texto del campo de entrada
    if dato:  # Verificar que el campo no esté vacío
        lista.insert(tk.END, dato)  # Añadir el dato a la lista
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo no puede estar vacío.")

# Función para limpiar la lista y el campo de texto
def limpiar_datos():
    lista.delete(0, tk.END)  # Borrar todos los elementos de la lista
    entry.delete(0, tk.END)  # Limpiar el campo de texto

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Datos")
ventana.geometry("400x300")

# Crear y colocar los componentes en la ventana
label = tk.Label(ventana, text="Ingrese información:")
label.pack(pady=10)

entry = tk.Entry(ventana, width=40)
entry.pack(pady=10)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

lista = tk.Listbox(ventana, width=50)
lista.pack(pady=20)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()