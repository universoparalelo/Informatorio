/*cambiando la ciudad donde vive de Luis Torres por Malaga*/
UPDATE `empresas`.`empleado`
SET
`CIUDAD` = "Málaga"
WHERE `NOMBRE_EMPLEADO` = "Luis Torres";

/*Dar a todos los empleados de la empresa `Facebook' un 10 % de aumento.*/
UPDATE empresas.trabaja 
SET 
sueldo = sueldo * 1.1
WHERE nombre_empresa = "Facebook";

/*Dar a todos los supervisores de la empresa `Microsoft' un 10 % de aumento.*/
UPDATE empresas.trabaja AS t
JOIN empresas.supervisa AS s ON t.nombre_empleado = s.nombre_empleado
SET t.sueldo = t.sueldo * 1.1
WHERE t.nombre_empresa = 'Microsoft';

/*Dar a todos los supervisores de la empresa `Google' un 10 % de aumento, a
menos que su salario supere los $1900, en ese caso, dar sólo un 3 % de
aumento.*/
UPDATE empresas.trabaja AS t
JOIN empresas.supervisa AS s ON t.nombre_empleado = s.nombre_empleado
SET sueldo = IF(sueldo>1900 AND nombre_empresa = "Google", sueldo*1.03, IF(sueldo<=1900 AND nombre_empresa = "Google", sueldo*1.1, sueldo))
WHERE NOMBRE_EMPRESA = "Google";

select * from empresas.supervisa;

