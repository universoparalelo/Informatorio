# Recibimos la frase que escriba el usuario y la convertimos a minusculas
frase = (input("Escriba un texto, parrafo o cadena de caracteres: ")).lower()

# Recibimos las letras que quiera buscar el usuario y las convertimos a minusculas
letras = list((input("Escriba tres caracteres: ")).lower())
# Iniciamos un contador en 0 para cada aparicion de cada letra
cont = [0,0,0]

# Loop para hallar la cantidad que aparece cada letra individualmente
for letra in frase:
    if letra == letras[0]:
        cont[0] += 1
    elif letra == letras[1]:
        cont[1] += 1
    elif letra == letras[2]:
        cont[2] += 1
    else: 
        pass

# Convertimos la frase a una cadena de palabras y contamos cuantas palabras hay
cant_palabras = len(frase.split(" "))  

# print(frase)
# print(letras)
print(f"La cantidad de veces que aparecio {letras[0]}: {cont[0]}")
print(f"La cantidad de veces que aparecio {letras[1]}: {cont[1]}")
print(f"La cantidad de veces que aparecio {letras[2]}: {cont[2]}")
print(f"La cantidad de palabras de la frase es: {cant_palabras}")

# Indice 0 para mostrar la primer letra o caracter de la frase
print(f"La primer letra de la frase es: {frase[0]}")

# Indice -1 para mostrar la ultima letra o caracter de la frase
print(f"La ultima letra de la frase es: {frase[-1]}")

# Se invierte la frase mediante indices
# Se indica que no se sabe donde se termina, un paso a la vez y que empiece por el final
frase_invertida = frase[::-1]

print(f"La frase inversa es: {frase_invertida}")

# Condicional para saber si la palabra "python" se encuentra en la frase
if ("python" in frase.split(" ")):
    print("La palabra python se encuentra en la frase")
else: 
    print("La palabra python no se encuentra en la frase")




