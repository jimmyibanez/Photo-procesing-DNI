import os

# Ruta de la carpeta que contiene los archivos .jpg
carpeta = "result"

# Lista para almacenar los nombres de los archivos
nombres_archivos = []

# Recorrer la carpeta y obtener los nombres de archivo .jpg
for archivo in os.listdir(carpeta):
    if archivo.endswith(".jpg"):
        nombres_archivos.append(archivo)

# Unir los nombres de archivo en una cadena separada por comas
lista_comas = ", ".join(nombres_archivos)

# Escribir la cadena en un archivo .txt
with open("lista_archivos.txt", "w") as archivo_txt:
    archivo_txt.write(lista_comas)

print("Se ha creado el archivo lista_archivos.txt con los nombres de los archivos.")
