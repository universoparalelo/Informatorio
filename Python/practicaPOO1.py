class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def mostrarDatos(self):
        print(f"Color: {self.color}")
        print(f"Cant. ruedas: {self.ruedas}")

#clase hija de Vehiculo
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def mostrarDatos(self):
        print(f"Velocidad max: {self.velocidad} km/h")
        print(f"Cilindrada: {self.cilindrada} cc")
        return super().mostrarDatos()

#clase hija de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def mostrarDatos(self):
        print(f"Tipo: {self.tipo}")
        return super().mostrarDatos()   

#clase hija de Coche
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def mostrarDatos(self):
        print(f"Carga: {self.carga} kg")
        return super().mostrarDatos() 

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrado):
        super().__init__(color, ruedas, tipo)   
        self.velocidad = velocidad
        self.cilindrado = cilindrado
    
    def mostrarDatos(self):
        print(f"Velocidad max: {self.velocidad} km/h")
        print(f"Cilindrada: {self.cilindrado} cc")
        return super().mostrarDatos()


# Ejercicios 1 ######################################

# vehiculo1 = Vehiculo('rojo', 4)
# vehiculo1.mostrarDatos()

# auto1 = Coche('blanco', 4, 260, 400)
# auto1.mostrarDatos()

# Ejercicio 2 #####################################

# auto1 = Coche('blanco', 4, 260, 400)
# bicicleta1 = Bicicleta('azul',2,'playera')
# camioneta1 = Camioneta('negro', 4, 200, 500, 5000)
# motocicleta1 = Motocicleta('blanco', 2, 'deportiva', 360, 300)

# vehiculos = []
# vehiculos.append(auto1)
# vehiculos.append(bicicleta1)
# vehiculos.append(camioneta1)
# vehiculos.append(motocicleta1)

# print(vehiculos)

# def catalogar(lista, cantRuedas):
#     cont = 0
#     for elemento in lista:
#         if elemento.ruedas == cantRuedas:
#             print(type(elemento))
#             elemento.mostrarDatos()
#             cont += 1
#     print(f"Se han encontrado {cont} vehiculos con {cantRuedas} ruedas")

# catalogar(vehiculos, 4)

# Ejercicio 3 ###################################
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def mostrarLadoMayor(self):
        lados = [self.lado1, self.lado2, self.lado3]
        print(f"El lado mayor es: {max(lados)}")

    def tipoTriangulo(self):
        if self.lado1 == self.lado2 and self.lado3 == self.lado1:
            print("El triangulo es equilatero")
        elif self.lado1==self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triangulo es isosceles")
        else: 
            print("El triangulo es escaleno")


# triangulos1 = Triangulo(12,12,10)
# triangulos2 = Triangulo(11,12,10)
# triangulos3 = Triangulo(12,12,12)

# triangulos1.mostrarLadoMayor()
# triangulos1.tipoTriangulo()
# triangulos2.mostrarLadoMayor()
# triangulos2.tipoTriangulo()
# triangulos3.mostrarLadoMayor()
# triangulos3.tipoTriangulo()

# Ejercicio 4 ##################################
class Tiempo:
    def __init__(self, hora, minutos, segundos):
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos    

    def cambiarHora(self, hora):
        self.hora = hora
# no termine este ejercicio

# Ejercicio 6 ####################################
class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"titular {self.titular}, cantidad {self.cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        
    def retirar(self, cantidad):
        self.cantidad -= cantidad

# cuenta1 = Cuenta('Celeste', 5000)
# cuenta1.mostrar()
# cuenta1.ingresar(8000)
# cuenta1.mostrar()
# cuenta1.retirar(1000)
# cuenta1.mostrar()

# Ejercicio 7 ####################################

class Bebidas:
    def __init__(self, id, cantLitros, precio, marca):
        self.id = id
        self.cantLitros = cantLitros
        self.precio = precio
        self.marca = marca
    
    def precioTotal(self):
        print(f"Precio total: {}")


class Agua(Bebidas):
    def __init__(self,bebida,origen):
        self.bebida = bebida
        self.origen = origen


class Gaseosas(Bebidas):
    def __init__(self, bebida, porcAzucar, tienePromo):
        self.bebida = bebida
        self.porcAzucar = porcAzucar
        self.tienePromo = tienePromo
        if self.tienePromo:
            self.precio *= 0.9

agua1 = Agua(1, 1.5, 450, 'Vital', 'Manantial')
# no termine este ejercicio

