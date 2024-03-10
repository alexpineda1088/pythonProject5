
# Definir los nombres de las ciudades, días de la semana y semanas
ciudades = ['Zamora', 'Cuenca', 'Machala']
dias_semana = ['Lunes ', 'Martes ', 'Miércoles ', 'Jueves', 'Viernes ', 'Sábado ', 'Domingo ']
semanas = 4
teperaturas= 21,24,23,24,25,24,27
# Crear la matriz 3D para almacenar las temperaturas
matriz_temperaturas = []

# Inicializar la matriz con valores de temperatura
for semana in range(semanas):
    semana_temperaturas =[]
    for ciudad in ciudades:
        ciudad_temperaturas =[]
        for dia in dias_semana:
            # Supongamos que inicialmente todas las temperaturas son 23
            ciudad_temperaturas.append(23 + 1)
        semana_temperaturas.append(ciudad_temperaturas)
    matriz_temperaturas.append(semana_temperaturas)

# Mostrar la matriz de temperaturas
print("Matriz de temperaturas:")
for semana, semana_temperaturas in enumerate(matriz_temperaturas):
    print(f"Semana {semana + 1}:")
    for ciudad_index, ciudad_temperaturas in enumerate(semana_temperaturas):
        print(f"  {ciudades[ciudad_index]}:")
        for dia_index, temperatura in enumerate(ciudad_temperaturas):
            print(f"    {dias_semana[dia_index]}: {temperatura}°C")


def calcular_temperatura_promedio(temperaturas):
    if not temperaturas:
        return None
    total_temperaturas = sum(temperaturas)
    temperatura_promedio = total_temperaturas / len(temperaturas)
    return temperatura_promedio


# Datos de temperaturas históricas
temperaturas_historicas = [21,24,23,24,25,24,27]

# Calcular la temperatura promedio utilizando la función definida
temperatura_promedio = calcular_temperatura_promedio(temperaturas_historicas)

# Imprimir el resultado
if temperatura_promedio:
    print("La temperatura promedio es:", temperatura_promedio)
else:
    print("No hay datos de temperatura para calcular.")