'''Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
sus ventas totales y el departamento comercial te solicita que ayudes a los
vendedores a calcular sus comisiones creando un programa que les pregunte su
nombre y cuánto han vendido en éste mes.
Tu programa le va a responder con una frase que incluya su nombre y el monto
que le corresponde por las comisiones
'''

# nombre = input("Escriba su nombre: ")
# vendido = float(input("Ingrese el monto total de lo vendido en el mes: "))

# print(f"Felicidades {nombre}, este mes has vendido ${vendido} y tu sueldo sera ${vendido * 0.06}")

'''Escribe un programa que solicite al usuario su información personal, incluyendo
su nombre completo, edad, estatura, peso, dirección y número de teléfono.
A continuación, el programa deberá imprimir un mensaje con los datos
ingresados por el usuario en el siguiente formato:
'''

nombre = input("Escriba su nombre: ")
edad = input("Escriba su edad: ")
estatura = input("Escriba su estatura: ")
peso = input("Escriba su peso: ")
direccion = input("Escriba su direccion: ")
num_tel = input("Escriba su num_tel: ")

print("\n++++++++++++++++++++++++++\n")

print(f"Nombre: {nombre}")
print(f"Edad: {edad} anios")
print(f"Estatura: {estatura} m")
print(f"Peso: {peso} kg")
print(f"Direccion: {direccion}")
print(f"Numero telefonico: {num_tel}")
