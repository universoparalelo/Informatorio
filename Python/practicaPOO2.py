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

    def pedido_preparado(self):
        total = 0
        print(f"{self.nombreCliente} su pedido esta listo")
        print("Mostrando su ticket")
        for i in range(self.cantPizzas):
            subtotal = self.nombre[i].get_precio(self.tipos[i],self.tamaños[i])
            print(f"{self.nombre[i]}  {self.tamaños[i]}  {self.tipos[i]}  {subtotal}")
            total += subtotal
        print(f"Total ${total}")

pizzaNapolitana = Pizza('napolitana', ['queso', 'jamopn','aceitunas'], ['grande', 'mediana', 'chica'], [[1000, 700, 500],[1100,800,600],[1200,900,700]], ['a la piedra', 'a la parrilla', 'de molde'])
pizzaMuzzarella = Pizza('muzzarella', ['queso', 'albahaca'], ['grande', 'mediana'], [[900,600],[800,500],[1000,700]], ['a la piedra', 'a la parrilla', 'de molde'])

menu = Menu()

menu.agregar_pizza(pizzaNapolitana)
menu.agregar_pizza(pizzaMuzzarella)

menu.mostrar_pizzas()

pedido1 = Pedido('celeste', 4, ['napolitana', 'napolitana', 'napolitana', 'muzzarella'], ['grande', 'grande', 'mediana', 'grande'], ['a la parrilla', 'a la parrilla', 'a la parrilla', 'a la parrilla'])
pedido1.mostrar_demora()
pedido1.pedido_preparado()