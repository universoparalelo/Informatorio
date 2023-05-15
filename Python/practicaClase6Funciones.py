'''1-Crea una función llamada suma que tome dos números como parámetros y
devuelva la suma de ellos.'''

# def suma(num1, num2):
#     return num1+num2

# print(suma(1,2))

'''2-Crea una función llamada saludo que tome el nombre de una persona como
parámetro e imprima un saludo personalizado.'''

# def respuesta(nombre):
#     print(f"Hola {nombre}, como estas?")

# nombre = input("EScribe tu nombre: ")
# respuesta(nombre)

'''3-Crea una función llamada invertir_cadena que tome una cadena de texto como
parámetro y devuelva la cadena invertida.'''

# def cadena_invertida(cadena):
#     cadena = cadena[::-1]
#     return cadena

# cadena = input("Escriba una cadena de texto: ")
# print(cadena_invertida(cadena))

'''4-Crea una función llamada es_capicua que tome un número como parámetro y
devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
derecha a izquierda) y False en caso contrario.'''

# def es_capicua(numero):
#     if numero == str(numero)[::-1]: print("Es capicua")
#     else: print("No es capicua")

# es_capicua(input("Escriba un numero entero: "))

'''5-Crea una función llamada es_divisible que tome dos números enteros como
parámetros y devuelva Es divisible si el primer número es divisible por el
segundo número, o No es divisible en caso contrario.'''

# def es_divisible(num1, num2):
#     if num1%num2 == 0:
#         return True
#     else: False

# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))

# resultado = es_divisible(num1,num2)
# if resultado:
#     print(f"{num1} es divisible por {num2}")
# else: print(f"{num1} no es divisible por {num2}")

'''6-Crea una función llamada es_par que tome un número como parámetro y
devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
devuelva Es impar o No es par'''

# def es_par(numero):
#     if numero%2 == 0:
#         return True
#     else: False

# numero = int(input("Escriba un numero: "))
# resultado = es_par(numero)

# if resultado: print(f"{numero} es par")
# else: print(f"{numero} no es par")

'''7-Crea una función llamada imprimir_pares que tome un número entero como
parámetro y imprima todos los números pares desde 1 hasta ese número.'''

# from funciones import imprimir_pares

# numero = int(input("Escriba un numero: "))
# imprimir_pares(numero)

'''8-Crea una función llamada es_palindromo que tome una cadena de texto como
parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
contrario.'''

# def es_palindromo(cadena):
#     if cadena == cadena[::-1]: return True
#     else: return False

# cadena = input("Escriba una cadena de texto: ")
# resultado = es_palindromo(cadena)

# if resultado: print("Es palindromo")
# else: print("No es palindromo")

'''9-Crea una función llamada promedio que tome una lista de números como
parámetro y devuelva el promedio de esos números.'''

# from funciones import promedio

# lista_num = input("Escriba una lista de numero separados por comas: ").split(',')
# resultado = promedio(lista_num)
# print(f"El promedio es: {resultado}")

'''10-Crea una función llamada calcular_factorial que tome un número entero como
parámetro y devuelva el factorial de ese número. El factorial de un número
entero positivo n se define como el producto de todos los números enteros
positivos desde 1 hasta n.'''

# from funciones import calcular_factorial

# numero = int(input(f"Ingrese un numero :"))
# print(f"El factorial es: {calcular_factorial(numero)}")

'''11-Crea una función llamada contar_vocales que tome una cadena de texto como
parámetro y devuelva el número de vocales que contiene.'''

# from funciones import contar_vocales

# cadena = input("Escriba una cadena de texto: ")
# resultado = contar_vocales(cadena)

# print(f"Cantidad de vocales en la cadena: {resultado}")

'''12-Crea una función llamada convertir_temperatura que tome una temperatura
en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
es: Fahrenheit = (Celsius * 9/5) + 32.'''

# def convertir_temp(temp):
#     return (temp * 9/5) + 32

# temp = float(input("Temperatura en Celsius: "))
# print(f"Temperatura Fahrenheit: {convertir_temp(temp)}")

'''13-Crea una función llamada calcular_descuento que tome dos parámetros:
precio y porcentaje_descuento. La función debe calcular y devolver el precio
después de aplicar el descuento.'''

# def calcular_descuento(precio, porc_desc):
#     return precio * ((100 - porc_desc)/100)

# precio = float(input("Precio: "))
# porc_desc = int(input("Porcentaje de descuento: "))
# print(f"El precio con descuento: {calcular_descuento(precio, porc_desc)}")

'''14-Crea una función llamada encontrar_maximo que tome una lista de números
como parámetro y devuelva el número máximo de la lista.'''

# from funciones import encontrar_maximo

# lista_num = input("Ingrese una lista de numeros separados con comas: ").split(",")
# print(f"El maximo numero de su lista es: {encontrar_maximo(lista_num)}")

'''15-Crea una función llamada contar_palabras que tome una cadena de texto
como parámetro y devuelva el número de palabras que contiene. Se considera
que las palabras están separadas por espacios.
'''

# def contar_palabras(cadena):
#     return len(cadena.split(" "))

# cantidad = contar_palabras(input("Ingrese un texto: "))
# print(f"Cantidad de palabras: {cantidad+1}")

'''16-Crea una función llamada eliminar_duplicados que tome una lista como
parámetro y devuelva una nueva lista sin duplicados, conservando el orden
original.'''

# from funciones import eliminar_duplicados

# lista_original = [1,2,3,4,1,5,'celeste','hola','celeste','1']
# nueva_lista = eliminar_duplicados(lista_original)
# print(f"Lista original: {lista_original}")
# print(f"Lista sin duplicados: {nueva_lista}")

'''17-Crea una función llamada es_anagrama que tome dos cadenas de texto como
parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
letras pero en distinto orden), o False en caso contrario.'''

# from funciones import es_anagrama

# cadena1 = input("Ingrese una cadena de texto: ")
# cadena2 = input("Ingrese otra cadena de texto: ")

# if es_anagrama(cadena1, cadena2):
#     print(f"'{cadena1}' y '{cadena2}' son anagramas")
# else: print(f"'{cadena1}' y '{cadena2}' no son anagramas")

'''18-Crea una función llamada calcular_mayor_diferencia que tome una lista de
números como parámetro y devuelva la mayor diferencia entre el numero mas
alto y el numero mas bajo en la lista.'''

# from funciones import calcular_max_diferencia

# lista = input("Escriba una lista de numeros separados por comas: ").split(",")
# print(f"Mayor diferencia: {calcular_max_diferencia(lista)}")

'''19-Crea una función llamada es_bisiesto que tome un año como parámetro y
devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario. Un año
es bisiesto si es divisible por 4, pero no por 100, a menos que también sea
divisible por 400.'''

from funciones import es_bisiesto
    
anio = int(input("Escriba un anio: "))

if es_bisiesto(anio):
    print(f"El anio {anio} es bisiesto!")
else:
    print(f"El anio {anio} no es bisiesto")