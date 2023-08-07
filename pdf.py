def obtener_archivos_pdf(file_path):
    archivos_pdf = []
    with open(file_path, "r") as file:
        for line in file:
            nombre_archivo, id_archivo = line.strip().split()
            if nombre_archivo.lower().endswith(".pdf"):
                archivos_pdf.append((nombre_archivo, id_archivo))
    return archivos_pdf

def guardar_archivos_pdf_en_txt(resultados, output_file):
    with open(output_file, "w") as file:
        for nombre_archivo, id_archivo in resultados:
            file.write(f"{id_archivo}\n")

# Reemplaza "ruta_del_archivo.txt" con la ruta real de tu archivo de texto.
archivo_texto = "data.txt"
archivos_pdf_con_ids = obtener_archivos_pdf(archivo_texto)

# Nombre del archivo de salida donde se guardarán los resultados.
archivo_salida = "fotos_pdf.txt"

# Guardar los resultados en el archivo plano de texto.
guardar_archivos_pdf_en_txt(archivos_pdf_con_ids, archivo_salida)

print("Resultados guardados en el archivo:", archivo_salida)

