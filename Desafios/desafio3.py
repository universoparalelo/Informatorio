import random

nombre = input("Ingrese su nombre: ")

print("Tiene que adivinar un numero del 1 al 100, y tiene 8 intentos")
print("Si ingresa un numero que no es entero saldra un error")
print("Si ingresa un numero valido pero no es el correcto se le descontara un intento")
print("Al final se le mostrara el numero correcto en el caso de que no haya adivinado")

num_rand = random.randint(1,100)

for i in range(8,0,-1):
    numero = input("Ingrese un numero entero: ")
    while not numero.isdigit():
        numero = input("Ingrese un numero entero valido: ")
    numero = int(numero)
    if numero < num_rand:
        print("El numero correcto es mayor.")
    elif numero > num_rand:
        print("El numero correcto es menor.")
    else:
        print(f"{nombre} adivinaste el numero, felicitaciones!!!")
        break
    if (i-1 == 0):
        print(f"{nombre} ya no tienes mas vidas. :(")
        print(f"El numero correcto era: {num_rand}")
    else:
        print(f"{nombre} tienes {i-1} intentos.")

