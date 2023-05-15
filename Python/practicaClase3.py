'''1-Escribir un programa que pida al usuario su edad y muestre por pantalla si es
mayor de edad (18 años o más) o no.'''

# edad = int(input("Ingrese su edad: "))

# if (edad >= 18):
#     print("Usted es mayor de edad")
# else:
#     print("No es mayor de edad")

'''2-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es positivo, negativo o cero.'''

# numero = int(input("Ingrese un numero entero cualquiera: "))

# if (numero < 0):
#     print("El numero es negativo.")
# elif (numero > 0):
#     print("El numero es positivo.")
# else:
#     print("El numero ingresado es cero.")

'''3-Escribir un programa que pida al usuario dos números y muestre por pantalla
cuál de ellos es mayor.'''

# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))

# if (num1 < num2):
#     print(f"El mayor es {num2}")
# else:
#     print(f"El numero mayor es {num1}")

'''4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
pantalla si está aprobado (5 o más) o no.'''

# nota = int(input("Ingrese su nota: "))

# if (nota < 6 and nota > 0):
#     print(f"Lo sentimos tu nota {nota} esta desaprobada dentro del sistema educativo, pero recuerda que es solo un numero. Sigue adelante!")
# elif (nota >= 6 and nota <= 10):
#     print(f"Tu nota {nota} es aprobado, felicitaciones!")
# else:
#     print(f"Su nota {nota} no existe =)")

'''5-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es par o impar.'''

# numero = int(input("Ingrese un numero entero: "))

# if (numero % 2 == 0):
#     print(f"El numero {numero} es par")
# else:
#     print(f"El numero {numero} es impar")

'''6-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es múltiplo de 2 y de 3 a la vez.'''

# numero = int(input("Ingrese un numero entero: "))

# if (numero%2 == 0 and numero%3 == 0):
#     print(f"{numero} es multiplo de 2 y 3 a la vez")
# else:
#     if (numero%2 == 0):
#         print(f"{numero} es multiplo de 2")
#     elif (numero%3 == 0):
#         print(f"{numero} es multiplo de 3")
#     else: 
#         print(f"{numero} no es multiplo de 2 ni de 3")

'''7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
es una letra mayúscula, una letra minúscula, un número o un carácter especial.'''

# caracter = ord(input("Ingrese un caracter: "))
# caracter = input("Ingrese un caracter: ")

# if (caracter < 58 and caracter > 47):
#     print(f"{chr(caracter)} es un numero")
# elif (caracter < 91 and caracter > 64):
#     print(f"{chr(caracter)} es una letra mayuscula")
# elif (caracter < 123 and caracter > 96):
#     print(f"{chr(caracter)} es una letra minuscula")
# else:
#     print(f"{chr(caracter)} es un caracter especial")

# if caracter.isalpha():
#     if caracter.isupper():
#         print(f"{caracter} es una letra mayuscula")
#     else:
#         print(f"{caracter} es una letra minuscula")
# elif caracter.isdigit():
#     print(f"{caracter} es un numero")
# else:
#     print(f"{caracter} es un caracter especial")

'''8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
por pantalla si contiene la letra "a".'''

# cadena = input("Ingrese una cadena de caracteres: ")

# if (cadena.find('a') == -1):
#     print(f"El caracter 'a' no se encuentra en la cadena")
# else:
#     print(f"El caracter 'a' se encuentra en la cadena")

'''9-Escribir un programa que pida al usuario tres números y muestre por pantalla
el mayor de ellos.'''

# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese un numero: "))
# num3 = int(input("Ingrese un numero: "))

# if (num1 > num2 and num1 > num3):
#     print(f"{num1} es el mayor")
# elif (num2 > num1 and num2 > num3):
#     print(f"{num2} es el mayor de todos")
# elif (num3 > num1 and num3 > num2):
#     print(f"{num3} es el mayor")
# else:
#     print("Los numeros ingresados son iguales")

'''10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
una vocal o una consonante.'''

# caracter = input("Ingrese una letra: ")

# if (caracter.casefold() in 'aeiou'):
#     print(f"{caracter} es una vocal")
# else:
#     print(f"{caracter} es una consonante")

'''11-Escribir un programa que pida al usuario dos números y muestre por pantalla
la suma de ellos solo si ambos son pares.'''

# num1 = int(input(f"Ingrese un numero: "))
# num2 = int(input(f"Ingrese un numero: "))

# if (num1%2 == 0 and num2%2== 0):
#     print(f"La suma de {num1}+{num2}= {num1+num2}")
# else:
#     print("Alguno o los dos numeros no son pares")
