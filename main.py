# Programa 2: Ordenación de Arreglo Multidimensional

# Definir la matriz bidimensional
matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Implementar función de ordenación de una fila específica (usando Bubble Sort)
def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar la fila a ordenar (por ejemplo, la primera fila)
fila_a_ordenar = 0

# Ordenar la fila seleccionada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz con fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
