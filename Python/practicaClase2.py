# EJERCICIO 11
'''Crea un programa que pida al usuario una palabra y muestre en pantalla
cuántas letras tiene.'''

# palabra = input("Ingrese cualquier palabra: ")

# print(f"La cantidad de letras es: {len(palabra)}")

# EJERCICIO 12
'''Escribe un programa que solicite al usuario su fecha de nacimiento en formato
dd/mm/aaaa y luego imprima su edad en años.'''

# anio_nac = input("Ingrese su fecha de nacimiento(dd/mm/aaaa): ")
# anio = anio_nac.split('/')

# print(f"Su edad es: {2023 - int(anio[2])}")

# EJERCICIO 13
'''Escribe un programa que solicite al usuario su nombre y su edad, y luego
imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.'''

# nombre = input("Escriba su nombre: ")
# edad = int(input("Ingrese su edad: "))

# print(f"Dentro de diez años {nombre} vas a tener {edad+10}!!!")

# EJERCICIO 14
'''Escribe un programa que solicite al usuario un número entero y luego
imprima el doble y el triple de ese número.'''

# numero = int(input("Ingrese un numero: "))

# print(f"El doble del numero es {numero*2}, el triple del mismo {numero*3}")

# EJERCICIO 15
'''Escribe un programa que solicite al usuario una temperatura en grados
Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.
'''

# temp_celsius = int(input("Ingrese una temperatura en Celsius: "))

# print(f"La temperatura en Farenheit: {(temp_celsius*1.8)+32}F")
# print(f"Y en grados Kelvin: {temp_celsius+273.15}K")

# EJERCICIO 16
'''-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
e imprima su índice de masa corporal (IMC).
La fórmula para calcular el IMC es: IMC = peso / (altura ** 2)'''

# peso = float(input("Ingrese su peso en kilogramos: "))
# altura = float(input("Ingrese su altura en metros: "))

# print(f"Su indice de masa corporal es: {peso/(altura*2)}")

# EJERCICIO 17
'''Escribe un programa que solicite al usuario palabras y luego las imprima
en orden inverso.'''

# palabras = input("Ingrese palabras: ")
# pal_separadas = palabras.split(" ")
# lista_reversa = list(reversed(pal_separadas))
# palabras = " ".join(lista_reversa)

# print(f"Las palabras en reversa sera: {palabras}")

# EJERCICIO 18
'''Crea un programa que pida al usuario su nombre, su edad y su ciudad de
residencia, y lo muestre en pantalla Utilizando una sola línea de código.
*Recuerda el print() del ejercicio anterior'''

# nombre = input("Ingrese su nombre: ")
# edad = input("Ingrese su edad: ")
# residencia = input("Ingrese su residencia: ")

# print(f"Bienvenido {nombre}, su edad es {edad} y vive en {residencia}.")

# EJERCICIO 19
'''Escribe un programa que solicite al usuario un número decimal y luego
imprima la parte entera y decimal por separado.'''

numero_decimal = float(input("Ingrese un numero decimal: "))
parte_entera = int(numero_decimal)%numero_decimal # 23 % 23.43
parte_decimal = numero_decimal - int(numero_decimal) # 23.43 - 23

print(f"La parte entera del numero {numero_decimal} es {parte_entera} y su parte decimal {parte_decimal}")
print("hola "+"mundo" *3)