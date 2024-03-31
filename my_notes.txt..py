# Escritura de Archivo de Texto
# Abrir el archivo en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribir algunas notas personales en el archivo
    file.write("Nota 1: Hoy tengo que ir hacer un deposito en el banco.\n")
    file.write("Nota 2: Recordar que tengo que tomar la pastilla despues de las 12 pm.\n")
    file.write("Nota 3: Preparar la presentación para el trabajo de fundmentos .\n")

# Lectura de Archivo de Texto
# Abrir el archivo en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leer el contenido del archivo línea por línea
    for line in file:
        # Mostrar en la consola cada línea leída
        print(line.strip())  # strip() elimina los caracteres de nueva línea al final de la línea

# Cierre de Archivo
# El archivo se cierra automáticamente cuando se sale del bloque with
