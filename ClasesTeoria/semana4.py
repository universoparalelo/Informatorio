# Modelado base de datos

# Modelo MER (modelado entidades-relacion)

# entidad: objeto con existencia fisica o conceptual (persona, empresa, cliente, universidad)
# atributos: caracteristicas que describen una entidad

## compuestos: atributos que son descritos a su vez por otros atributos (fecha de nacimiento)
## simples: atributos que no se pueden subdividir (edad, nombre, dni)

## monovaluados: atributos que no pueden ser mas de uno por entidad (edad, nombre)
## multivaluados: atributos que pueden ser mas de uno por entidad (telefono por persona, correo por persona)

## almacenados: atributos que no se pueden calcular a partir de otro atributo (fecha de nacimiento)
## derivados: atributos que se pueden calcular a partir de otro atributo (edad a partir de fecha de nac.)

## clave: conjunto de atributos minimos para identificar una entidad de otras del mismo tipo

# relacion: asociacion entre dos o mas entidades
## unitaria: grado 1
## binaria: grado 2
## ternario: grado 3
## N-arias: grado N

## cardinalidad: número de entidades con las que puede estar relacionada una entidad dada.

### 1-1: Un registro de una entidad A se relaciona con solo un registro en una entidad B.
### 1-N: Un registro en una entidad en A se relaciona con cero o muchos registros en una entidad B. Pero los registros de B solamente se relacionan con un registro en A.
### N-1: Una entidad en A se relaciona exclusivamente con una entidad en B. Pero una entidad en B se puede relacionar con 0 o muchas entidades en A.
### N-M: Una entidad en A se puede relacionar con 0 o con muchas entidades en B y viceversa.

## Atributos propios de una relacion: atributos cuyo valor sólo se puede obtener en la relación, puesto que dependen de todas las entidades que participan en la relación.

# Una ENTIDAD FUERTE es aquella que no necesita de otra entidad débil para existir.
# Una ENTIDAD DEBIL es aquella que sí que necesita de otra para existir.
 