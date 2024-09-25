cadena1 = str(input("Escriba una cadena de texto: "))
cadena2 = str(input("Escriba otra cadena de texto: "))
numero = int(input("Escriba un número"))
cadena1valida = len(cadena1) >= 5 and len(cadena1) <= 10
cadena2valida = cadena2[0].isupper()
numeropositivo = numero >= 0
divisibilidad3 = numero % 3 == 0
divisibilidad5 = numero % 5 == 0
numvalido = numeropositivo and (divisibilidad3 or divisibilidad5)

print("La primera cadena de texto ingresada tiene entre 5 a 10 caracteres?: ",cadena1valida)
print("La segunda cadena de texto tiene su primera letra (dentro del alfabeto Español) como una mayúscula?: ", cadena2valida)
print("El número dado es positivo?: ",numeropositivo)
print("El número dado es divisible entre 3?: ",divisibilidad3)
print("El número dado es divisible entre 5?: ",divisibilidad5)
print("El número cumple con todos los criterios?: ",numvalido)