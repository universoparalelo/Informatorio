import datetime

class Usuario:
    def __init__(self, nombre=None, apellido=None, telefono=None, username=None, email=None, contraseña=None, avatar=None):
        self.id = id
        self.__nombre = None
        self.__apellido = None
        self.__telefono = None
        self.__username = None
        self.__email = None
        self.__contraseña = None
        self.__f_registro = datetime.datetime.now()
        self.__avatar = None
        self.__estado = True
        self.__online = False
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    
    def setApellido(self, apellido):
        self.__apellido = apellido
    def getApellido(self):
        return self.__apellido
    
    def setTelefono(self, telefono):
        self.__telefono = telefono
    def getTelefono(self):
        return self.__telefono
    
    def setUsername(self, username):
        self.__username = username
    def getUsername(self):
        return self.__username
    
    def setEmail(self, email):
        self.__email = email
    def getEmail(self):
        return self.__email
    
    def setContraseña(self, contraseña):
        self.__contraseña = contraseña
    def getContraseña(self):
        return self.__contraseña
    
    def setF_registro(self, f_registro):
        self.__f_registro = f_registro
    def getF_registro(self):
        return self.__f_registro
    
    def setAvatar(self, avatar):
        self.__avatar = avatar
    def getAvatar(self):
        return self.__avatar

    def setEstado(self, estado):
        self.__estado = estado
    def getEstado(self):
        return self.__estado
    
    def setOnline(self, online):
        self.__online = online
    def getOnline(self):
        return self.__online

    def login(self, nombre, contraseña, lista):
        for usuario in lista:
            if (usuario.getUsername() == nombre) and (usuario.getContraseña() == contraseña):
                return True
        return False

    def registrar(self):
        self.setNombre(input("Escriba su nombre: "))
        self.setApellido(input("Escriba su apellido: "))
        self.setTelefono(input("Escriba su telefono: "))
        self.setUsername(input("Escriba su username: "))
        self.setEmail(input("Esciba su email: "))
        self.setContraseña(input("Escruba su contraseña: "))
        self.setAvatar(input("Escriba su avatar: "))
        
    
class Publico(Usuario):
    def __init__(self, nombre, apellido, telefono, username, email, contraseña, avatar):
        super().__init__(nombre, apellido, telefono, username, email, contraseña, avatar)
        self.__es_publico = True

    def setEsPublico(self, es_publico):
        self.__es_publico = es_publico
    def getEsPublico(self):
        return self.__es_publico
        
    def comentar(self):
        print("Su comentario se subio correctamente.")
        print("----------------------------------------------")


class Colaborador(Usuario):
    def __init__(self, nombre, apellido, telefono, username, email, contrasena, avatar):
        super().__init__(nombre, apellido, telefono, username, email, contrasena, avatar)
        self.__es_colaborador = True

    def setEsColaborador(self, es_colaborador):
        self.__es_colaborador = es_colaborador
    def getEsColaborador(self):
        return self.__es_colaborador

    def comentar(self):
        print("Su comentario se subio correctamente.")
        print("----------------------------------------------")
        

    def publicar(self, titulo):
        print(f"Su articulo '{titulo}' se subio correctamente.")
        print("----------------------------------------------")


class Articulo:
    def __init__(self, titulo, resumen, contenido, imagen):
        self.id = None
        self.id_usuario = None
        self.__titulo = titulo
        self.__resumen = resumen
        self.__contenido = contenido
        self.__f_publicacion = datetime.datetime.now()
        self.__imagen = imagen
        self.__estado = True
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
    def getTitulo(self):
        return self.__titulo
    
    def setResumen(self, resumen):
        self.__resumen = resumen
    def getResumen(self):
        return self.__resumen
    
    def setContenido(self, contenido):
        self.__contenido = contenido
    def getContenido(self):
        return self.__contenido
    
    def setImagen(self, imagen):
        self.__imagen = imagen
    def getImagen(self):
        return self.__imagen
    
    def setF_publicacion(self, f_publicacion):
        self.__f_publicacion = f_publicacion
    def getF_publicacion(self):
        return self.__f_publicacion
    
    def setEstado(self, estado):
        self.__estado = estado
    def getEstado(self):
        return self.__estado
    

class Comentario:
    def __init__(self, contenido):
        self.id = None 
        self.id_articulo = None
        self.id_usuario = None
        self.__contenido = contenido
        self.fecha_hora = datetime.datetime.now()
        self.estado = True
    
    def setContenido(self, contenido):
        self.__contenido = contenido
    def getContenido(self):
        return self.__contenido


cont = 0
contAr = 0
contCom = 0


def Menu():
    rta = 0
    rta2 = 0
    rta3 = 0 
    rta4 = 0
    listaUsuario = []
    listaPublico = []
    listaColaborador = []
    listaPublicaciones = []
    listaComentarios = []

    while rta != 3:
        print("Bienvenido al Blog")
        print("1. Registrar")
        print("2. Login")
        print("3. Salir")

        rta = int(input("Escoja un numero: "))
    
        if rta == 1:
            print("--------------- Registro ------------------")
            rta2 = int(input("Que tipo de usuario quiere crear 1.Publico / 2.Colaborador: "))
            if rta2 == 1:
                usuario = Publico('x', 'x', 'x', 'x', 'x', 'x','x')
                usuario.id = cont + 1
                usuario.registrar()
                listaPublico.append(usuario)
            elif rta2 == 2:
                usuario = Colaborador('x', 'x', 'x', 'x', 'x', 'x','x')
                usuario.id = cont + 1
                usuario.registrar()
                listaColaborador.append(usuario)
            listaUsuario.append(usuario)
            print("Usuario registrado")
            print("-------------------------------------------")

        elif rta == 2:
            print("------------------ Login ------------------")
            nombre = input("Username: ")
            contraseña = input("Contraseña: ")
            if (usuario.login(nombre, contraseña, listaUsuario)):
                usuario.setOnline(True)
                print(f"{usuario.getUsername()} esta logeado")
                rta3 = int(input("¿Que desea realizar ahora? 1.Publicar | 2.Leer articulos: "))
            else: print("Error. Usuario o contraseña incorrecto")
            print("---------------------------------------")

            try:
                if rta3 == 1 and usuario.getEsColaborador():
                    print("--------------- Publicacion ------------------")
                    publicacion = Articulo('x','x','x','x')
                    publicacion.id = contAr + 1
                    publicacion.id_usuario = usuario.id
                    publicacion.setTitulo(input("Titulo: "))
                    publicacion.setContenido(input("Contenido: "))
                    publicacion.setImagen(input("Url de la imagen: "))
                    listaPublicaciones.append(publicacion)
                    usuario.publicar(publicacion.getTitulo())
                
                elif rta3 == 2:
                    print("------------------ Lista de articulos -------------------")
                    for articulo in listaPublicaciones:
                        print(f"Id: {articulo.id}")
                        print(f"Fecha de publicacion: {articulo.getF_publicacion()}")
                        print(f"Titulo: {articulo.getTitulo()}")
                        print(f"Contenido: {articulo.getContenido()}")
                        print("----------------------------------------------------")
                    rta4 = int(input("Si desea comentar en algunos de ellos coloque el ID o si quiere volver al menu principal escriba 0: "))

                    if rta4 == 0:
                        continue
                    else:
                        print("---------------- Comentarios ------------------")
                        comentario = Comentario('x')
                        comentario.id = contCom + 1
                        comentario.id_usuario = usuario.id
                        comentario.id_articulo = publicacion.id
                        comentario.setContenido(input("Contenido: "))
                        listaComentarios.append(comentario)
                        usuario.comentar()
            except AttributeError:
                print("No puede realizar ninguna publicacion, ya que su cuenta es de tipo Publico")
                print("-------------------------------------------------------")

        else:
            break


Menu()