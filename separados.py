def organizar_horizontalmente(input_file, output_file):
    # Leer los datos del archivo .txt
    with open(input_file, "r") as file:
        data = file.read().splitlines()

    # Concatenar los datos con comas para obtener una línea horizontal
    datos_horizontal = ",".join(data)

    # Escribir los datos organizados horizontalmente en el archivo de salida
    with open(output_file, "w") as file:
        file.write(datos_horizontal)

# Reemplaza "archivo_entrada.txt" con la ruta real de tu archivo .txt
archivo_entrada = "fotos_pdf.txt"

# Reemplaza "archivo_salida.txt" con el nombre que deseas para el archivo de salida
archivo_salida = "separados.txt"

# Organizar los datos horizontalmente y guardarlos en el archivo de salida
organizar_horizontalmente(archivo_entrada, archivo_salida)

print("Datos organizados horizontalmente y guardados en:", archivo_salida)
