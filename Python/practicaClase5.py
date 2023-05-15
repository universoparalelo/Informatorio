'''1-Escribe un programa que pida al usuario una palabra y luego imprima cada
letra de la palabra en una línea separada.'''

# palabra = input("Escriba cualquier palabra: ")

# print("Imprimiendo cada letra>>>>>>>>>>>>")
# for letra in palabra:
#     print(letra)

'''2-Escribe un programa que pida al usuario un número y calcule la suma de todos
los números naturales del 1 hasta ese número.'''

# numero = int(input("Escriba un numero natural: "))
# sum = 0
# for num in range(numero+1):
#     sum += num

# print(f"La suma de todos los naturales hasta {numero} es: {sum}")

'''3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
multiplicar correspondiente a ese número del 1 al 10.'''

# numero = int(input("Escriba un numero para conocer su tabla de multiplicar: "))

# for num in range(1,11):
#     print(f"{numero} x {num} = {numero*num}")

'''4-Escribe un programa que imprima los números pares del 1 al 100.'''

# for i in range(1,101):
#     print(i)

'''5-Escribe un programa que imprima la suma de todos los números pares del 1 al
100.'''

# sum = 0

# for i in range(2,101,2):
#     sum += i

# print(sum)

'''6-Escribe un programa que pida al usuario una palabra y luego imprima la misma
palabra pero con las letras en orden inverso.'''

# palabra = input("Escriba cualquier palabra: ")

# for i in range(len(palabra), 0, -1):
#     print(palabra[i-1])

'''7-Escribe un programa que pida al usuario una palabra y determine si es un
palíndromo'''

# palabra = input("Escriba cualquier palabra: ").lower()
# nueva_palabra = ''

# for i in range(len(palabra), 0, -1):
#     nueva_palabra += palabra[i-1]

# print(nueva_palabra)

# if (palabra == nueva_palabra):
#     print("La palabras ingresada SI es un palindromo")
# else:
#     print("La palabra que ingreso NO es un palindromo")

'''8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
el número de palabras que contiene.'''

# texto = input("Escriba cualquier cadena de texto: ")
# cont_palabras = 0

# for caracter in texto:
#     if (caracter == " " ):
#         cont_palabras += 1

# print(f"La cantidad de palabras del texto es: {cont_palabras+1}")

'''9-Escribe un programa que pida al usuario un número y luego imprima la
secuencia de Fibonacci correspondiente a ese número.'''

# x = 1
# y = 0
# z = 0

# numero = int(input("Ingrese la cantidad de digitos que quiere ver de la secuencia fibonacci: "))

# for i in range(numero):
#     print(x+z) # 1 + 0
#     y = x
#     x = z+x
#     if i == 0: continue
#     else: z = y

'''10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con todas las vocales en mayúscula.'''

# texto = input("Escriba cualquier cadena de texto: ").lower()
# nuevo_texto = ""

# for i in texto:
#     if i in ['a', 'e', 'i', 'o', 'u']:
#         i = i.upper()
#     nuevo_texto += i

# print(f"Texto con las vocales en mayusculas: {nuevo_texto}")

'''11-Escribe un programa que pida al usuario un número y calcule su factorial.'''

# numero = int(input("Escriba un numero natural: "))
# factorial = 1

# for num in range(1,numero+1):
#     factorial *= num

# print(f"El factorial de {numero} es: {factorial}")

'''12-Escribe un programa que pida al usuario una lista de números separados por
comas y calcule su promedio.
'''
# numeros = input("Escriba una lista de numeros separados con comas: ").split(',')
# sum = 0
# cont = 0

# for num in numeros:
#     sum += int(num)
#     cont += 1

# print(f"Promedio de los numeros: {sum/cont}")

'''13-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de asteriscos con esa cantidad de filas.
*
**
***
****
*****'''

# numero = int(input("Ingrese un numero: "))

# for i in range(numero):
#     for j in range(i+1):
#         print('*', end="")
#     print("")

'''14-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de números como el siguiente:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
# numero = int(input("Ingrese un numero: "))

# for i in range(numero):
#     for j in range(i+1):
#         print(f"{i+1} ", end="")
#     print("")

'''Pedimos un rango de numeros para mostrar el mismo patron'''
# numero1 = int(input("Ingrese un numero inicial: "))
# numero2 = int(input("Ingrese un numero final: "))

# for i in range(numero1-1, numero2):
#     for j in range(i+1):
#         print(f"{i+1} ", end="")
#     print("")

'''15-Escribe un programa que pida al usuario una cadena de texto y determine
cuántas veces aparece cada letra en la cadena.'''

# texto = input("Escriba algo: ")
# dicc = dict()

# for letra in texto:
#     if letra == " ":
#         pass
#     dicc[letra] = 0

# for letra in texto:
#     if letra == " ":
#         pass
#     dicc[letra] += 1

# print(dicc)

'''16-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con cada palabra al revés.'''

# palabra = input("Escriba cualquier palabra: ")
# palabra = palabra[::-1]

# print(palabra)

'''17-Escribe un programa que pida al usuario una cadena de texto y luego imprima
la misma cadena pero con las palabras en orden inverso.'''

# texto = input("Escriba una cadena de texto: ").split(" ")
# texto_inverso = list()

# for i in range(len(texto),0,-1):
#     texto_inverso.append(texto[i-1])

# print(texto_inverso)

'''18-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de números como el siguiente:
1
2 3
4 5 6
7 8 9 10'''

# numero = int(input("Ingrese un numero: "))
# num = 0

# for i in range(numero):
#     for j in range(i+1):
#         num += 1
#         print(f"{num} ", end="")
#     print("")

'''19-Escribe un programa que pida al usuario un número y luego imprima si ese
número es un número perfecto o no.'''

# numero = int(input("Escriba un numero: "))
# divisores = 0

# for i in range(1,numero):
#     if numero%i == 0:
#         divisores += i
    
# if divisores == numero:
#     print(f"El numero es perfecto. {numero}={divisores}")
# else:
#     print(f"El numero no es perfecto. {numero}!={divisores}")

'''Buscando numeros perfectos'''

# numero = int(input("Escriba hasta donde quiere buscar numeros perfectos: "))
# divisores = 0
# num_perfectos = list()

# for j in range(6,numero):
#     divisores = 0
#     for i in range(1,j):
#         if j%i == 0:
#             divisores += i
#     if divisores == j:
#         num_perfectos.append(j)

# print(f"Numeros perfectos: {num_perfectos}")



























