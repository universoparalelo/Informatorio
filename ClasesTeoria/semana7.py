# mysql

# a partir del modelado con MER
# hacemos las tablas

# pasaje de mer a tablas

# una relacion N:M se transforma en una tabla, donde las filas seran los atributos claves de cada entidad y los atributos de la relacion propia

# una relacion 1:N no crea una tabla intermedia, solo se agrega una clave foranea(atributo clave) de la entidad fuerte en la tabla de la entidad debil.

# una relacion 1:1 no se crea una tabla intermedia pero cada entidad tendra una clave foranea de la otra entidad para identificar la pertenencia

# SINTAXIS DEL SQL (structure query language)

# tipos de datos (mas comunes)
'''
VARCHAR(n): cadena de hasta 'n' caracteres
CHAR(n): cadena de 'n' caracteres si o si
INT: numeros enteros
FLOAT(p): numero con decimales de precision p
DATE: almacena fecha YYYY-MM-DD
TIME: almacena en formato HH:MM:SS
BOOLEAN: verdadero o falso
'''

# TIPOS DE SENTENCIAS
#DML - manipulacion de datos
'''
SELECT - recuperar datos de la base de datos
INSERT - añade nuevas filas de datos a la base de datos
DELETE - suprime ciertas filas de la base de datos
UPDATE - modifica datos existentes en la base de datos
'''
#DDL - definicion de datos
'''
CREATE TABLE - añade una nueva tabla a la base de datos
DROP TABLE - suprime una tabla a la base de datos
ALTER TABLE - modifica la estructura de una tabla existente
CREATE VIEW - añade una nueva vista a la base de datos
DROP VIEW - suprime una vista de la base de datos
CREATE INDEX - contruye un indice para una columna
DROP INDEX - suprime el indice para una columna
'''
#DCL - control de acceso y control de transacciones
'''
GRANT - concede privilegios de acceso a usuarios
REVOKE - suprime privilegios de acceso a usuarios
COMMIT - finaliza la transaccion actual
ROLLBACK - aborta la transaccion actual
'''
'''
sintaxis de un pedido a mysql

SELECT CURSO, NOMBRE, NOTA FROM ALUMNO
  WHERE ASIGNATURA = "PLE"

verbo | nombre de las columnas | clausula | nombre de la tabla 
palabra reservada | expresion | constante

'''

