# Crear el diccionario
informacion_personal = {
    "nombre": "Alexander Pineda",
    "edad": 30,
    "ciudad": "Cuenca",
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "Ingeniero"

# Verificar la existencia de la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0980348996"

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)
