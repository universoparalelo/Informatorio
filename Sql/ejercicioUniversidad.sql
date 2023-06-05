-- Lista las asignaturas del tipo "optativa".
select * from asignatura where tipo like "optativa";

-- Lista los nombres de Departamento de la Universidad.
select * from departamento;

-- Listar apellidos y nombre de las Personas, convirtiendo ambos elementos a mayúsculas
select upper(nombre), upper(apellido1), upper(apellido2) from persona;

-- Listar apellidos y nombres de Profesores mayores a 40 años en la Universidad.
select distinct persona.nombre, persona.apellido1, persona.apellido2, persona.fecha_nacimiento 
from persona, profesor
where (fecha_nacimiento - 2023/06/03) >= 40;

