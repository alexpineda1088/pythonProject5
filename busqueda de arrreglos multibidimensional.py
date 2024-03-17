# Programa 1: Búsqueda en Arreglo Multidimensional

# Definir la matriz bidimensional
matriz = [
    [6, 2, 8],
    [4, 7, 1],
    [5, 3, 9]
]

# Implementar función de búsqueda
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return True, i, j
    return False, None, None

# Valor a buscar
valor_a_buscar = 5

# Realizar búsqueda
encontrado, fila, columna = buscar_valor(matriz, valor_a_buscar)

# Mostrar resultados
if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la fila {fila + 1}, columna {columna + 1}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
