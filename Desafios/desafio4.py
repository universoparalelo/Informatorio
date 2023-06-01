
def menu():
    rta = 0
    while rta != 5:
        print("************* Bienvenido a la inmobiliaria *************")
        print("1. Agregar un inmueble")
        print("2. Editar un inmueble")
        print("3. Eliminar un inmueble")
        print("4. Busqueda")
        print("5. Salir")

        rta = int(input("Seleccione la opcion que desea: "))

        if rta == 1:
            crearInmueble()
        elif rta == 2:
            editarInmueble(inmuebles)
        elif rta == 3:
            eliminarInmueble(inmuebles)
        elif rta == 4:
            precio = int(input("Escriba el maximo que quiere gastar: "))
            inmueblesDisponibles = busqueda(inmuebles,precio)
            if inmueblesDisponibles == []:
                print("No existe ningun inmueble disponible para ese presupuesto.")
                
            else:
                print("Imprimiendo todos los inmuebles disponibles: ")
                i = 1
                for inmueble in inmueblesDisponibles:
                    print(f"{i}. {inmueble}")
                    i += 1
                input("Presione enter para seguir operando...")

# Funcion para crear un inmueble
def crearInmueble():
    dict_inmueble={"año":int(input("Ingrese antiguedad del inmueble: ")),
                   "metros":int(input("Ingrese los metos cuadrados del inmueble: ")),
                    "habitaciones":int(input("Ingrese el numero de habitaciones: ")),
                    "garaje":bool(input("tiene garaje si o no (True/False): ")),
                    "zona":input("Es de zona A B o C: ").upper(),
                    "estado":input("Su estado es Disponible , Reservado o Vendido: ").lower().capitalize()}
    
    validarInmueble(inmuebles,dict_inmueble)

# Funcion para validar un inmueble que se quiere agregar
def validarInmueble(listaInmuebles,inmuebleParaAgregar):
    if (inmuebleParaAgregar['zona']== "A" or inmuebleParaAgregar['zona']== "B" or inmuebleParaAgregar['zona']== "C"):
        if (inmuebleParaAgregar['estado']=="Disponible" or inmuebleParaAgregar['estado']=="Reservado" or inmuebleParaAgregar['estado']=="Vendido"):
            if (int(inmuebleParaAgregar['año']) >= 2000) and (int(inmuebleParaAgregar['metros']) >= 60) and (int(inmuebleParaAgregar['habitaciones']) >= 2):
                if inmuebleParaAgregar['garaje'] == True or inmuebleParaAgregar['garaje'] == False:
                    listaInmuebles.append(inmuebleParaAgregar)
                    print("El inmueble se agregó correctamente.")
                else: 
                    print("No se puede agregar el inmueble a la lista")   

# Funcion para editar un valor de un inmueble
def editarInmueble(listaInmuebles):
    print("Seleccione cual inmueble quiere editar, ingresando el numero de indice que figura en el menú: ")
    for i in range(0,len(listaInmuebles)):
        print(f" * {i}- {listaInmuebles[i]}")

    # Guarda el inmueble elegido por el usuario
    inmuebleAEditar= int(input("Ingrese el numero de inmueble a editar: "))

    print(f"Inmueble a editar\n {listaInmuebles[inmuebleAEditar]}")

    listaDeEditables=["año","metros","habitaciones","garage","zona","estado"]

    for i in range(0,6):
        print(i,listaDeEditables[i])

    # Guarda el nombre del campo a editar
    itemAEditar= input("Ingrese el nombre del campo que desea editar: ").lower()
    
    inmuebles[inmuebleAEditar][itemAEditar] = input("Escriba el nuevo valor de manera correcta: ")

    # Se elimina el inmueble que se edito, se lo guarda y se manda a verificar
    inmuebleaVerificar = inmuebles.pop(inmuebleAEditar)
    validarInmueble(inmuebles, inmuebleaVerificar)

# Funcion para eliminar un inmueble
def eliminarInmueble(listaInmuebles):
    print("Seleccione cual inmueble quiere eliminar, ingresando el numero de indice que figura en el menú: ")
    for i in range(0,len(listaInmuebles)):
        print(f" * {i}- {listaInmuebles[i]}")

    inmuebleAEditar= int(input("Ingrese el numero de inmueble a eliminar: "))
    listaInmuebles.pop(inmuebleAEditar)
    print("El inmueble se elimino correctamente.")
    print(inmuebles)

# Funcion para buscar inmuebles basados en un precio maximo
def busqueda(listaInmueble, precioMaximo):
    inmueblesDisponibles = list()
    for inmueble in listaInmueble:
        if inmueble['garaje'] == True:
            inmueble['precio'] = (int(inmueble['metros']) * 100 + int(inmueble['habitaciones']) * 500 + int(inmueble['garaje']) * 1500) * (inmueble['año']/100 - 1)
        else:
            inmueble['precio'] = (int(inmueble['metros']) * 100 + int(inmueble['habitaciones']) * 500) * (inmueble['año']/100 -1)
        
        if inmueble['zona'] == 'B': inmueble['precio'] * 1.5
        elif inmueble['zona'] == 'C': inmueble['precio'] * 2

        if inmueble['precio'] <= precioMaximo and (inmueble['estado'] == "Disponible" or inmueble['estado'] == "Reservado"):
            inmueblesDisponibles.append(inmueble)
    
    return inmueblesDisponibles
            

inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

menu()




