# Crear la clase para luego poder instanciar Personas
class Persona:
# Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
# Método
    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.')
# Metodo para mostrar atributos del objeto
    def __str__(self):
        return f"nombre: {self.nombre}, edad: {self.edad} años"
        
# Metodo para settear un atributo
    def set_legajo(self,edad):
        return f"nombre {self.nombre}, edad {edad}"



################################################

# Crear una instancia de la clase Persona
personal = Persona("Juan", 25)

# Acceder a los atributos de la instancia
print(personal.nombre) #Imprime: Juan
print(personal.edad) # Imprime: 25

# Llamar a un método de Ia instancia
personal.saludar() # Imprime: Hola, mi nombre es Juan y tengo 25 años!.

# Como no especifico que quiero ver de personal utiliza por defecto el metodo __str__
print(personal)

# Cambia un atributo solo un momento
print(personal.set_legajo(20))

