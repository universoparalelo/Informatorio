# Ejercicio 1 ####################################

import datetime

class Pizza:
    def __init__(self, nombre, ingredientes, tamaños, precios, tipo):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.tamaños = tamaños
        self.precios = precios
        self.tipo = tipo

    def get_precio(self, tipo, tamaño):
        t = 0
        p = 0
        for i in range(len(self.tipo)):
            if self.tipo[i] == tipo:
                break
            t += 1
        for j in range(len(self.tamaños)):
            if self.tamaños[j] == tamaño:
                break
            p += 1
        return self.precios[t][p]
        


class Menu:
    def __init__(self):
        self.pizzas = []

    def agregar_pizza(self, nuevaPizza):
        self.pizzas.append(nuevaPizza)

    def mostrar_pizzas(self):
        for i in range(len(self.pizzas)):
            print(f"Nombre: {self.pizzas[i].nombre}")
            print(f"Ingredientes: '{self.pizzas[i].ingredientes}'")
            print("              ", end="")
            for j in range(len(self.pizzas[i].tamaños)):
                print(f"{self.pizzas[i].tamaños[j]}", end="  ")
            for k in range(len(self.pizzas[i].tipo)):
                print(f"\n{self.pizzas[i].tipo[k]}", end="  ")
                for z in range(len(self.pizzas[i].precios[k])):
                    print(f"${self.pizzas[i].precios[k][z]}", end="     ")
            print("\n-------------------------------------------")
                

class Pedido:
    def __init__(self, nombreCliente, cantPizzas, nombrePizzas, tamaño, tipo):
        self.nombreCliente = nombreCliente
        self.cantPizzas = cantPizzas
        self.nombre = nombrePizzas
        self.tamaños = tamaño
        self.tipos = tipo
        self.hora = datetime.time()
        self.demora = self.cantPizzas * 10
        self.entregada = False
    
    def mostrar_demora(self):
        print(f"La demora de su pedido tardará aproximadamente {self.demora}min")
        print("-------------------------------------------------------------------")

    def pedido_preparado(self):
        total = 0
        print(f"{self.nombreCliente} su pedido esta listo")
        print("****************Mostrando su ticket************************")
        for i in range(self.cantPizzas):
            subtotal = self.nombre[i].get_precio(self.tipos[i],self.tamaños[i])
            print(f"{self.nombre[i].nombre}  {self.tamaños[i]}  {self.tipos[i]}  {subtotal}")
            total += subtotal
        print(f"Total ${total}")
        print("-------------------------------------------------------------------")

class Informe:
    def __init__(self):
        self.pedidos = []
        self.menu = None
    
    def agregarPedido(self, nuevoPedido):
        self.pedidos.append(nuevoPedido)
    
    def actualizar_menu(self, menuNuevo):
        self.menu = menuNuevo
    
    def informe_variedadesTipos(self):
        pass
        

# napolitana = Pizza('napolitana', ['queso', 'jamopn','aceitunas'], ['grande', 'mediana', 'chica'], [[1000, 700, 500],[1100,800,600],[1200,900,700]], ['a la piedra', 'a la parrilla', 'de molde'])
# muzzarella = Pizza('muzzarella', ['queso', 'albahaca'], ['grande', 'mediana'], [[900,600],[800,500],[1000,700]], ['a la piedra', 'a la parrilla', 'de molde'])

# menu = Menu()

# menu.agregar_pizza(napolitana)
# menu.agregar_pizza(muzzarella)

# menu.mostrar_pizzas()

# pedido1 = Pedido('celeste', 4, [napolitana, napolitana, napolitana, muzzarella], ['grande', 'grande', 'mediana', 'grande'], ['a la parrilla', 'a la parrilla', 'a la parrilla', 'a la parrilla'])
# pedido1.mostrar_demora()
# pedido1.pedido_preparado()

# EJERCICIO 2 ##############################################################################

class Producto:
    def __init__(self, nombre, precio, esParte = False):
        self.nombre = nombre
        self.precio = int(precio)
        self.esParte = esParte


class Supermercado:
    def __init__(self, nombre, direccion):
        self.nombre = nombre 
        self.direccion = direccion 
        self.productos = []

    def agregar_producto(self, nuevoProducto):
        self.productos.append(nuevoProducto)

    def aplicar_descuento(self, producto, descuento):
        for i in range(len(self.productos)):
            if producto == self.productos[i]:
                if self.productos[i].esParte:
                    self.productos[i].precio *= (1 - (int(descuento)/100))
    
    def mostrar_productos(self):
        print("Mostrando productos")
        for i in range(len(self.productos)):
            print("-------------------------------------")
            print(f"Nombre producto: {self.productos[i].nombre}")
            print(f"Precio: {self.productos[i].precio}")
            if self.productos[i].esParte:
                print("El producto es parte del Programa Precios Cuidados")
            else:
                print("El producto NO es parte del Programa Precios Cuidados")
            print("-------------------------------------")

    def suma_productos(self):
        suma_total = 0
        for i in range(self.productos):
            suma_total += self.productos[i].precio
        print(f"Precio total de todos los productos {suma_total}")
        print("-------------------------------------")
        


# EJERCICIO 3 ###############################################################################

class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo 
    
    def __str__(self):
        print(f"{self.numero}, {self.palo}")
        print("------------------------")
    
class Baraja:
    def __init__(self):
        self.cartas = []

    def agregarCarta(self, nuevaCarta):
        self.cartas.append(nuevaCarta)

    def mostrarBaraja(self):
        print("Mostrando baraja")
        print(f"{self.cartas}")
        print("----------------------------------")

carta1 = Carta(2,'basto')
carta2 = Carta(3, 'oro')
carta3 = Carta(5, 'espada')
carta4 = Carta(10, 'copas')

baraja1 = Baraja()
baraja1.agregarCarta(carta1)
baraja1.agregarCarta(carta2)
baraja1.agregarCarta(carta3)
baraja1.agregarCarta(carta4)

baraja1.mostrarBaraja()

# EJERCICIO 4 #################################################################################

# EJERCICIO 5 #################################################################################

