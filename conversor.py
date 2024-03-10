
def conversor(grados_cent):
  Fahrenheit = (9 / 5) * (grad_cent) + 32_#transformar centigrados a feren
  kelvin = 273.15 + grados_cent  #transformacion de grados centigrados a kelvin
  return Fahrenheit, kelvin

  centigrados=int(input("ingrese grados en centigrados=")

resul_far, result_kelvin = conversor(centigrados)

print(centigrados, "grados centigrados es igual a", result_far, "grados Fahrenheit")
print("kelvin" , result_kelvin)
