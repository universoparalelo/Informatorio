'''1-Crear un diccionario con los nombres de tres frutas y sus respectivos precios y mostrar el diccionario completo.
'''

# dictionary = {"banana": 300, "manzana": 700, "mandarinas": 500}

# print("***************Mostrando diccionario****************")

# for key,value in dictionary.items():
#     print(f"{key}: ${value}")

'''2-Crear una lista con los nombres de tres ciudades y agregar una cuarta ciudad al final de la lista.'''

# ciudades = ["Buenos Aires", "Corrientes", "Parana"]
# print(ciudades)

# ciudades.append("Resistencia")
# print(ciudades)

'''3-Crear una lista con los nombres de tres países y mostrar el segundo país de la lista.'''

# paises = ["Alemania", "Brasil", "Peru"]
# print(paises[1])

'''4-Crear un diccionario con los nombres de tres personas y sus respectivas edades. Mostrar la edad de la tercera persona en el diccionario.'''

# diccionario = {"Celeste": 20,
#                "Bianca": 20,
#                "Ludmila": 19}
# print(diccionario["Ludmila"])

'''5-Crear un set/conjunto con los números del 1 al 10 y mostrar el número más grande en el conjunto.'''

# numeros = {1,2,99,3,4,10,5,6,7,8,9}
# print(sorted(list(numeros)).pop())

'''6-Crear un set/conjunto con los números impares del 1 al 10 y mostrar el número de elementos en el conjunto.'''

# numeros = {1,2,3,4,5,7,6,9,8,10,115}
# print(len(numeros))

'''7-Crear un diccionario con los nombres de tres ciudades y sus respectivas poblaciones. Agregar una cuarta ciudad al diccionario con su respectiva población. Mostrar el diccionario resultante.'''

# ciudades = {"Alemania": "alemanes",
#             "Brasil": "brasileños",
#             "Argentina": "argentinos"}
# ciudades["Peru"] = "peruanos"

# print(ciudades)

'''8-Crear una lista con los números del 1 al 10 y mostrarlos en orden inverso.'''

# numeros = {1,2,3,4,5,6,7,8,9,10}
# numeros = list(numeros)
# numeros = numeros[::-1]
# print(numeros)

'''9-Crear una lista con los nombres de tres países y ordenar la lista en orden alfabético. Mostrar la lista resultante.'''

# paises = ['Noruega', 'Mexico', 'Guatemala', 'Holanda']
# print(sorted(paises))

'''10-Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la lista. Mostrar la lista resultante'''

# frutas = ["banana", "manzana", "mandarinas", "ciruela"]
# print(frutas)
# del frutas[1]
# print(frutas)

'''11-Crear una lista con los nombres de tres animales y agregar una cuarta animal al principio de la lista. Mostrar la lista resultante.'''

# animales = ["leon", "tigre", "halcon", "puercoespin", "dorado"]
# print(animales)
# animales.insert(0, "tiburon")
# print(animales)

'''12-Crear una lista con los nombres de tres países y reemplazar el segundo país de la lista por otro país. Mostrar la lista resultante.'''

# paises = ["Alemania", "Bolivia", "Argentina"]
# paises[1] = "Chile"

# print(paises)

'''13-Crear una lista con los nombres de tres colores y agregar dos colores más al final de la lista. Mostrar la lista resultante.'''

# colores = ["azul", "amarillo", "verde"]
# colores.append("marron")
# colores.append("rojo")
# print(colores)

'''14-Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los elementos de la tupla.'''

# numeros = (1,2,3,4,5,15)
# suma = 0

# for numero in numeros:
#     suma += numero

# print(f"La suma de todos los elementos es: {suma}")

'''Ejercicio extra'''

# diccionario = dict()
# diccionario["nombre"] = "Celeste"
# diccionario["materias"] = ["AM2", "SSL", "F2", "IyS", "AnSI"]
# diccionario["notas"] = [[9,8,8],[7,8,7],[6,6,6],[8,9,8],[6,7,8]]

# print(f"Mostrando las notas de {diccionario['nombre']}")

# for i in range(0,5):
#     print(f"{diccionario['materias'][i]}: {diccionario['notas'][i]}")
# print(f"{diccionario['materias'][1]}: {diccionario['notas'][1]}")


    
