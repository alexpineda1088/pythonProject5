
# Definir los nombres de las ciudades, días de la semana y semanas
ciudades = ['Zamora', 'Cuenca', 'Machala']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Crear la matriz 3D para almacenar las temperaturas
matriz_temperaturas = []

# Inicializar la matriz con valores de temperatura
for semana in range(semanas):
    semana_temperaturas =[]
    for ciudad in ciudades:
        ciudad_temperaturas =[]
        for dia in dias_semana:
            # Supongamos que inicialmente todas las temperaturas son 22
            ciudad_temperaturas.append(22)
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