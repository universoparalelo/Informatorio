# estructuras repetitivas

# WHILE. se ejecuta hasta que su condicion sea falsa

# while (condicion):
#     acciones

'''DENTRO DE LAS ACCIONES SE DEBE EN ALGUN MOMENTO MODIFICAR
LOS VALORES DE LA CONDICION'''

# PROGRAMA QUE MUESTRE LOS PRIMEROS 10 NUMEROS

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

# FOR EN PYTHON, FUNCIONA CON CUALQUIER VARIABLE ITERABLE
'''
que datos son iterables?
-strings
-listas
-tuplas
-diccionarios
-rangos
'''
# range(valor inicial, valor final, cada cuantos pasos)
# range(1,11) --> [1,2,3,4,5,6,7,8,9,10]
for contador in range(1,11):
    print(contador)

for letras in "Celeste":
    print(letras)