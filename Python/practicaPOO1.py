import math

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
    def __init__(self, hora, minutos = 0, segundos = 0):
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos    

    def __str__(self):
        return f"Hora: {self.hora}, Minutos: {self.minutos}, Segundos: {self.segundos}"

    def __set_hora(self, hora):
        self.hora = hora

class prueba_tiempo(Tiempo):
    def __init__(self, hora, minutos=0, segundos=0):
        super().__init__(hora, minutos, segundos)

    def cambiar_hora(self):
        print(self)
        self._Tiempo__set_hora(input("Modifique la hora: "))
        print(self)


# tiempo1 = Tiempo(14, 30, 55)
# print(tiempo1)
# tiempo1._Tiempo__set_hora(13)
# print(tiempo1)

# nuevaHora = prueba_tiempo(14,50)
# nuevaHora.cambiar_hora()

# Ejercicio 5 ####################################

class Alimentos:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def Calcular(self, entidades):
        cantPorEnt = 0
        cantidad = self.cantidad
        for i in range(0,len(entidades)):
            cantPorEnt = math.ceil(cantidad / (len(entidades) - i))
            cantidad -= cantPorEnt
            print(f"{entidades[i]}: {cantPorEnt}", end=", ")
    

class Perecedero(Alimentos):
    def __init__(self, nombre, cantidad, diasCaducar):
        self.diasCaducar = diasCaducar
        super().__init__(nombre, cantidad)

    def Calcular(self, entidades):
        super().Calcular(entidades)
        
        if self.diasCaducar < 10:
            print("\nLa entrega debe hacerse en el dia actual")
        elif self.diasCaducar == 30:
            print("\nLa entrega debe hacerse en el plazo de 1 semana")


class NoPerecedero(Alimentos):
    def __init__(self, nombre, cantidad, tipo):
        super().__init__(nombre, cantidad)
        self.tipo = tipo

    def Calcular(self, entidades):
        super().Calcular(entidades)
        print("\nLa fecha de entrega queda libre de eleccion siempre que no supere el mes")

        
# perecedero1 = Perecedero('arroz', 13, 9)
# perecedero1.Calcular(('entidad1', 'entidad2', 'entidad3'))

# no_perecedero1 = NoPerecedero('arroz', 13, 10)
# no_perecedero1.Calcular(('entidad1', 'entidad2', 'entidad3'))

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

class Bebida:
    def __init__(self, identificador, litros, precio, marca):
        self.identificador = identificador
        self.litros = litros
        self.precio = precio
        self.marca = marca

    def calcular_precio(self):
        return self.precio

    def mostrar_informacion(self):
        print("Identificador:", self.identificador)
        print("Litros:", self.litros)
        print("Precio:", self.precio)
        print("Marca:", self.marca)


class AguaMineral(Bebida):
    def __init__(self, identificador, litros, precio, marca, origen):
        super().__init__(identificador, litros, precio, marca)
        self.origen = origen

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Origen:", self.origen)


class Gaseosa(Bebida):
    def __init__(self, identificador, litros, precio, marca, porcentaje_azucar, promocion=False):
        super().__init__(identificador, litros, precio, marca)
        self.porcentaje_azucar = porcentaje_azucar
        self.promocion = promocion

    def calcular_precio(self):
        if self.promocion:
            return self.precio * 0.9  # Descuento del 10% si hay promoción
        else:
            return self.precio

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Porcentaje de Azúcar:", self.porcentaje_azucar)
        print("Promoción:", "Sí" if self.promocion else "No")


class Almacen:
    def __init__(self):
        self.bebidas = []

    def calcular_precio_todas_bebidas(self):
        precio_total = 0
        for bebida in self.bebidas:
            precio_total += bebida.calcular_precio()
        return precio_total

    def calcular_precio_marca_bebida(self, marca):
        precio_total = 0
        for bebida in self.bebidas:
            if bebida.marca == marca:
                precio_total += bebida.calcular_precio()
        return precio_total

    def agregar_producto(self, bebida):
        if not self._existe_identificador(bebida.identificador):
            self.bebidas.append(bebida)
            print("Bebida agregada correctamente.")
        else:
            print("Error: El identificador ya existe.")

    def eliminar_producto(self, identificador):
        for bebida in self.bebidas:
            if bebida.identificador == identificador:
                self.bebidas.remove(bebida)
                print("Bebida eliminada correctamente.")
                return
        print("Error: No se encontró la bebida con ese identificador.")

    def mostrar_informacion_bebidas(self):
        for bebida in self.bebidas:
            bebida.mostrar_informacion()
            print("-------------------------")

    def _existe_identificador(self, identificador):
        for bebida in self.bebidas:
            if bebida.identificador == identificador:
                return True
        return False


# Ejemplo de uso
# almacen = Almacen()

# agua_mineral = AguaMineral("001", 1.5, 10.0, "Manantial", "Natural")
# gaseosa1 = Gaseosa("002", 2.0, 15.0, "Coca-Cola", 10, True)
# gaseosa2 = Gaseosa("003", 2.5, 12.0, "Pepsi", 8)

# almacen.agregar_producto(agua_mineral)
# almacen.agregar_producto(gaseosa1)
# almacen.agregar_producto(gaseosa2)

# print("Precio total de todas las bebidas:", almacen.calcular_precio_todas_bebidas())
# print("Precio total de la marca Coca-Cola:", almacen.calcular_precio_marca_bebida("Coca-Cola"))

# almacen.mostrar_informacion_bebidas()

# almacen.eliminar_producto("002")

# almacen.mostrar_informacion_bebidas()

# Ejercicio 8 #####################################

class Libro:
    def __init__(self, titulo, autor, numPaginas, calificacion):
        self.titulo = titulo
        self.autor = autor
        self.numPaginas = numPaginas
        self.calificacion = calificacion

    def __modificarDatos(self):
        print("""Que desea modoficar: 1.Titulo, 2.Autor, 3.Numero de paginas, 4.Calificacion """, end="")

        rta = int(input(": "))

        if rta == 1:
            self.titulo = input("Escriba el titulo: ")
        elif rta == 2:
            self.autor = input("Escriba el autor: ")
        elif rta == 3:
            self.numPaginas = input("Escriba el numero de paginas")
        else:
            self.calificacion = int(input("Ingrese la nueva calificacion: "))

        self.validarDatos(rta)
        self.mostrarDatos()
    
    def validarDatos(self, rta):
        valido = False
        while valido == False:
            if (type(self.autor) or type(self.titulo) == 'str') and (self.calificacion <= 10 and self.calificacion >= 0):
                valido = True
            else:
                if rta == 1:
                    self.titulo = input("Escriba el titulo: ")
                elif rta == 2:
                    self.autor = input("Escriba el autor: ")
                elif rta == 3:
                    self.numPaginas = input("Escriba el numero de paginas")
                else:
                    self.calificacion = int(input("Ingrese la nueva calificacion: "))


    def mostrarDatos(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Numero de paginas: {self.numPaginas}")
        print(f"Calificacion: {self.calificacion}")

class ConjuntoLibros:
    def __init__(self):
        self.libros = []

    def añadir_libro(self, libro):
        if (type(libro.autor) or type(libro.titulo) == 'str') and (libro.calificacion <= 10 and libro.calificacion >= 0):
            self.libros.append(libro)
            print("El libro se añadio correctamente.")
        else:
            print("No se puede añadir el libro.")
    
    def eliminar_libro(self,tit_aut):
        for i in range(0, len(self.libros)):
            if self.libros[i].autor == tit_aut or self.libros[i].titulo == tit_aut:
                self.libros.pop(i)
                print(f"El libro{i+1} se eliminó correctamente")
                break

    def mejorYpeor_libro(self):
        mejor = -1
        peor = 11
        mejorLibro = 0
        peorLibro = 0
        for i in range(0, len(self.libros)):
            if self.libros[i].calificacion > mejor:
                mejorLibro = i
                mejor = self.libros[i].calificacion
            elif self.libros[i].calificacion < peor:
                peorLibro = i
                peor = self.libros[i].calificacion
        print("El libro con mejor calificacion es:")
        self.mostrarLibro(mejorLibro)
        print("El libro con peor calificacion es:")
        self.mostrarLibro(peorLibro)

    def mostrarLibro(self, i):
        print(f"Titulo: {self.libros[i].titulo}")
        print(f"Autor: {self.libros[i].autor}")
        print(f"N de paginas: {self.libros[i].numPaginas}")
        print(f"Calificacion: {self.libros[i].calificacion}")

# miLibreria = ConjuntoLibros()

# libro1 = Libro('Cantar a un ruiseñor', "Brian Lee", 430, 10)
# libro2 = Libro('Lady Midnight', "Cassandra Clare", 530, 9)
# libro3 = Libro('Madame Bovary', "Gustave Flaubert", 300, 5)
# libro4 = Libro('Los siete locos', "Robert Arlt", 220, 6)
# libro5 = Libro('Anna Karenina', "Tolstoi", 850, 8)

# miLibreria.añadir_libro(libro1)
# miLibreria.añadir_libro(libro2)
# miLibreria.añadir_libro(libro3)
# miLibreria.añadir_libro(libro4)
# miLibreria.añadir_libro(libro5)

# miLibreria.mejorYpeor_libro()
# miLibreria.eliminar_libro('Madame Bovary')

# libro1.mostrarDatos()
# libro1._Libro__modificarDatos()

# Ejercicio 9 #####################################

class Cafetera:
    def __init__(self, capMaxima, cantActual):
        self.capMaxima = capMaxima
        self.cantActual = cantActual

    def llenarCafetera(self):
        print("Llenando cafetera.....")
        print(f"La cantidad actual de cafe es {self.cantActual}ml")
        self.cantActual = self.capMaxima
        print(f"La cantidad de cafe actual ahora es: {self.cantActual}ml")
        print("----------------------------------------")

    def servirTaza(self, intCafe):
        print("Sirviendo cafe.....")
        if (self.cantActual - intCafe) < 0:
            print(f"Disculpa no tengo suficiente cafe, solo te cargo {self.cantActual}ml")
            self.cantActual = 0
        else:
            self.cantActual -= intCafe
            print("Disfrute su cafe.")
        print("----------------------------------------")
    
    def vaciarCafetera(self):
        print("Vaciando cafetera....")
        print(f"La cantidad actual de cafe es {self.cantActual}ml")
        self.cantActual = 0
        print(f"La cantidad de cafe actual ahora es: {self.cantActual}ml")
        print("----------------------------------")
    
    def agregarCafe(self, intCafe):
        print("Agregando cafe....")
        print(f"Cantidad actual de cafe: {self.cantActual}ml")
        if (self.cantActual + intCafe) > self.capMaxima:
            print(f"Cantidad actual de cafe: {self.capMaxima}ml")
            self.cantActual = self.capMaxima
        else:
            self.cantActual += intCafe
            print(f"Cantidad actual de cafe: {self.cantActual}ml")
        print("----------------------------------------")

# cafetera1 = Cafetera(1000, 450)

# cafetera1.llenarCafetera()
# cafetera1.servirTaza(400)
# cafetera1.vaciarCafetera()
# cafetera1.agregarCafe(300)

# cafetera1.servirTaza(400)
# cafetera1.agregarCafe(1500)
# cafetera1.servirTaza(500)
# cafetera1.llenarCafetera()
# cafetera1.servirTaza(500)
# cafetera1.vaciarCafetera()

# Ejercicio 10 ####################################

class Mate:
    def __init__(self, cantYerba):
        self.yerba = cantYerba
        self.cantCebadas = round(cantYerba / 4)
        self.estado = False

    def cebar(self):
        print("Cebando un mate.....")
        if (self.cantCebadas - 1) == 0:
            print("El mate esta lavado.")
            self.cantCebadas = 0
        else:
            self.cantCebadas -= 1

        if self.estado == False:
            print("Disfruta tu mate.")
            self.estado = True
        else:
            print("Cuidado! Te quemaste!")
        print("--------------------------------")
    
    def beber(self):
        print("Tomando un mate.....")
        if self.estado == False:
            print("El mate esta vacio!")
        else:
            print("*Ruido de mate*")
            self.estado = False
        print("-------------------------------------")

# mate1 = Mate(20)

# mate1.cebar()
# mate1.beber()
# mate1.cebar()
# mate1.cebar()
# mate1.beber()
# mate1.beber()
# mate1.cebar()
# mate1.beber()
# mate1.cebar()
# mate1.beber()
from datetime import datetime
print(datetime.today())
