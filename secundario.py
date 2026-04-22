from tkinter import filedialog                 # selector de archivos

def abrir_pdf():                               # función para abrir pdf
    archivo_pdf = filedialog.askopenfilename(  # abre explorador
        filetypes=[("Archivos PDF", "*.pdf")]  # filtra pdf
    )
    print("Archivo seleccionado:", archivo_pdf) # muestra ruta
    return archivo_pdf                         # retorna archivo