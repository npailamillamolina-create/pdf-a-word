import tkinter as tk                               # librería para crear la interfaz gráfica
import os                                          # librería para trabajar con rutas y nombres de archivos
import secundario                                  # archivo secundario donde está la función para abrir el PDF
from pdf2docx import Converter                     # librería para convertir PDF a Word
from tkinter import filedialog, ttk               # filedialog para guardar archivo y ttk para barra de progreso

ventana = tk.Tk()                                  # crea la ventana principal
ventana.title("Convertir PDF a Word")              # pone título a la ventana
ventana.configure(bg="SkyBlue")                    # cambia el color de fondo
ventana.geometry("450x300")                        # define el tamaño de la ventana

label_style = {"bg": "SkyBlue", "fg": "black"}     # diccionario con estilo para los labels

label_importar = tk.Label(                         # crea label fijo
    ventana,                                       # dentro de la ventana
    text="Importa PDF",                            # texto del label
    **label_style                                  # aplica estilo
)
label_importar.grid(row=0, column=0, padx=10, pady=10)   # ubica el label en la grilla

label_importado = tk.Label(                        # crea label para mostrar mensajes
    ventana,                                       # dentro de la ventana
    text="",                                       # inicia vacío
    **label_style                                  # aplica estilo
)
label_importado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)   # ubica el label debajo

barra = ttk.Progressbar(                           # crea barra de progreso
    ventana,                                       # dentro de la ventana
    mode="indeterminate",                          # modo de movimiento continuo
    length=250                                     # largo de la barra
)
barra.grid(row=2, column=0, columnspan=2, padx=10, pady=10)   # ubica la barra
barra.grid_remove()                                # la oculta al iniciar

def convertir_pdf():                               # función principal para convertir el PDF
    archivo = secundario.abrir_pdf()               # abre el selector y recibe la ruta del PDF

    if archivo:                                    # verifica si el usuario sí seleccionó un archivo
        nombre_archivo = os.path.basename(archivo) # obtiene solo el nombre del archivo
        label_importado.config(text=f"PDF: {nombre_archivo}")   # muestra el nombre del PDF seleccionado

        nombre_word = os.path.splitext(nombre_archivo)[0] + ".docx"   # cambia la extensión a .docx

        ruta_guardado = filedialog.asksaveasfilename(   # abre ventana para elegir dónde guardar
            defaultextension=".docx",              # extensión por defecto
            filetypes=[("Word", "*.docx")],        # tipo de archivo permitido
            initialfile=nombre_word                # nombre sugerido para guardar
        )

        if ruta_guardado:                          # verifica si el usuario eligió una ruta de guardado
            barra.grid()                           # muestra la barra de progreso
            barra.start(10)                        # inicia el movimiento de la barra
            ventana.update_idletasks()             # actualiza la ventana para mostrar cambios

            cv = Converter(archivo)                # crea el convertidor usando el PDF seleccionado
            cv.convert(ruta_guardado)              # convierte el PDF a Word y lo guarda en la ruta elegida
            cv.close()                             # cierra el convertidor

            barra.stop()                           # detiene la barra de progreso
            barra.grid_remove()                    # oculta la barra otra vez

            nombre_final = os.path.basename(ruta_guardado)   # obtiene el nombre del Word creado
            label_importado.config(text=f"Word creado: {nombre_final}")   # muestra mensaje final

button_importa = tk.Button(                        # crea el botón principal
    ventana,                                       # dentro de la ventana
    text="Selecciona PDF",                         # texto del botón
    command=convertir_pdf                          # función que se ejecuta al hacer clic
)
button_importa.grid(row=0, column=1, padx=10, pady=10)   # ubica el botón al lado del primer label

ventana.mainloop()                                 # mantiene la ventana abierta y funcionando