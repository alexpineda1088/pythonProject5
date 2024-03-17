# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado al monto total de la compra.

    Args:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (float, opcional): Porcentaje de descuento a aplicar.
            Por defecto es 10%.

    Returns:
        float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función calcular_descuento desde el programa principal
# Llamada 1: Proporcionando solo el monto total de la compra
monto_compra_1 = 100
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1
print(f"monto total de la compra:{monto_compra_1}")
print(f"Monto del descuento 1: {descuento_1}")
print(f"Monto final a pagar después del descuento 1: {monto_final_1}")

# Llamada 2: Proporcionando tanto el monto total de la compra como el porcentaje de descuento
monto_compra_2 = 200
porcentaje_descuento_2 = 12
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2
print(f"monto total de la compra:{monto_compra_2}")
print(f"Monto del descuento 2: {descuento_2}")
print(f"Monto final a pagar después del descuento 2: {monto_final_2}")
