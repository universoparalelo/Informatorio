from mascota import ImagenMascota
import random

class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivelHambre = 0
        self.nivelFelicidad = 0
        self.imagen = ImagenMascota()
    
    def presentacion(self):
        print(f"Tu mascota se llama {self.nombre}")
        print(self.imagen.inicio)
        print("------------------------------------")
    
    def despedida(self):
        print("Adios, espero te hayas divertido!")
        print(self.imagen.feliz)

    def alimentar(self):
        self.nivelHambre -= random.randint(10,15)
        self.nivelFelicidad -= random.randint(5,10)

        if self.nivelHambre == 0:
            print("La mascota esta llena, no puede comer mas!")
            return self.imagen.feliz
        elif self.nivelHambre < 0:
            self.nivelHambre = 0

        print("La mascota fue alimentada!")
        print(self.imagen.feliz)
    
    def jugar(self):
        if self.nivelHambre < 70:
            self.nivelFelicidad += random.randint(10,25)
            self.nivelHambre += random.randint(10,15)

            if self.nivelFelicidad > 100:
                self.nivelFelicidad = 100
            if self.nivelHambre > 100:
                self.nivelHambre = 100
            print("Se divierte!")
            print(self.imagen.feliz)
        else:
            print("Tiene mucha hambre y no puede jugar")
            print(self.imagen.disgustado)
        
    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        if self.nivelFelicidad == 0 and self.nivelHambre == 0:
            print("Estado: 'tu mascota murio de hambre y falta de felicidad'")
            print(self.imagen.muerto)
        elif self.nivelHambre >= 70 and self.nivelFelicidad <= 50:
            print(f"Estado: 'muy hambriento y muy triste'")
            print(self.imagen.disgustado)
        elif self.nivelHambre >= 70:
            print(f"Estado: 'muy hambriento'")
            print(self.imagen.disgustado)
        elif self.nivelFelicidad <= 50:
            print(f"Estado: 'muy triste'")
            print(self.imagen.triste)
        else:
            print("Estado: 'contenta y satisfecha'")
            print(self.imagen.feliz)
        
      
# mascotaVirtual = MascotaVirtual('Firulais')

# mascotaVirtual.presentacion()
# mascotaVirtual.alimentar()
# mascotaVirtual.alimentar()
# mascotaVirtual.alimentar()
# mascotaVirtual.mostrar_estado()
# mascotaVirtual.jugar()
# mascotaVirtual.jugar()
# mascotaVirtual.jugar()
# mascotaVirtual.jugar()
# mascotaVirtual.jugar()
# mascotaVirtual.jugar()
# mascotaVirtual.alimentar()
# mascotaVirtual.alimentar()
# mascotaVirtual.mostrar_estado()

def Menu():
    while True:
        print("---------- Menu principal ------------")
        print("1. Crear tu mascota")
        print("2. Alimentar")
        print("3. Jugar")
        print("4. Mostrar estado")
        print("5. Despedida")

        rta = int(input("Elige una opcion: "))

        try:
            if rta == 1:
                mascota = MascotaVirtual(input("Nombre: "))
                mascota.presentacion()
            elif rta == 2:
                mascota.alimentar()
            elif rta == 3:
                mascota.jugar()
            elif rta == 4:
                mascota.mostrar_estado()
            else:
                mascota.despedida()
                break
        except UnboundLocalError:
            print("Debes crear una mascota antes de usar una funcion")

Menu()
