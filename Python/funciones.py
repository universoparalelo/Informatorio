def imprimir_pares(tope):
    print(f"Numeros pares desde 1 hasta {tope}: ", end="")
    for i in range(1,tope+1):
        if i%2 == 0:
            print(f"{i},", end="")


def contar_vocales(cadena):
    cont = 0
    for letra in cadena:
        if letra in "aeiou":
            cont += 1
    return cont


def promedio(lista):
    sum = 0
    cont = 0
    for i in lista:
        sum += int(i)
        cont += 1
    return sum/cont


def calcular_factorial(numero):
    factorial = 1
    for i in range(1,numero+1):
        factorial *= i
    return factorial


def encontrar_maximo(lista_num):
    max = -9999
    for num in lista_num:
        if int(num) > max:
            max = int(num)
    return max

def encontrar_minimo(lista_num):
    min = 99999
    for num in lista_num:
        if int(num) < min:
            min = int(num)
    return min


def eliminar_duplicados(lista):
    nueva_lista = list()
    for elemento in lista:
        if elemento in nueva_lista:
            pass
        else: 
            nueva_lista.append(elemento)
    return nueva_lista

def es_anagrama(cadena1, cadena2):
    cadena1 = cadena1.lower().replace(" ","")
    cadena2 = cadena2.lower().replace(" ","")
    bandera = True
    for letra in cadena1:
        if letra in cadena2:
            pass
        else:
            return False
    return True


def calcular_max_diferencia(lista):
    return encontrar_maximo(lista) - encontrar_minimo(lista)


def es_bisiesto(anio):
    if anio%4 == 0 and anio%100 != 0:
        return True
    elif anio%400 == 0:
        return True
    else:
        return False