import tkinter as tk                           # librería interfaz
import secundario                           # archivo secundario
import os                                     #manejo la ruta

ventana = tk.Tk()                             # crea ventana
ventana.title("Traductor de pdf")             # título
ventana.configure(bg="SkyBlue")               # fondo
ventana.geometry("400x300")                   # tamaño

label_style = {"bg": "SkyBlue", "fg": "black"}   # estilo visible

label_importar = tk.Label(ventana, text="Importa pdf", **label_style)   # texto fijo
label_importar.grid(row=0, column=0, padx=10, pady=10)                  # posición

label_importado = tk.Label(ventana, text="", **label_style)         # prueba visible
label_importado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)   # debajo

def manejar_pdf():                              # función botón
    archivo = secundario.abrir_pdf()           # abre selector
    
    if archivo:                                # si eligió archivo
        nombre_archivo = os.path.basename(archivo)  # obtiene nombre
        label_importado.config(text= nombre_archivo)   # cambia texto

button_importa = tk.Button(                    # crea botón
    ventana,
    text="Selecciona pdf",
    command=manejar_pdf
)
button_importa.grid(row=0, column=1, padx=10, pady=10)                  # posición

ventana.mainloop()                             # mantiene ventana