
CREATE TABLE cargo (
    idcargo     CHAR(3) NOT NULL,
    nombre      VARCHAR(50) NOT NULL,
    sueldo_min  FLOAT NOT NULL,
    sueldo_max  FLOAT NOT NULL,
    CONSTRAINT pk_cargo PRIMARY KEY ( idcargo )
);

CREATE TABLE ubicacion (
    idubicacion   CHAR(3) NOT NULL,
    ciudad        VARCHAR(50) NOT NULL,
    direccion     VARCHAR(100) NOT NULL,
    CONSTRAINT pk_ubicacion PRIMARY KEY ( idubicacion )
);

CREATE TABLE departamento (
    iddepartamento  INT NOT NULL,
    nombre          VARCHAR(100) NOT NULL,
    idubicacion     CHAR(3) NOT NULL,
    CONSTRAINT pk_departamento 
		PRIMARY KEY ( iddepartamento ),
    CONSTRAINT fk_departamento_ubicacion 
        FOREIGN KEY ( idubicacion ) 
        REFERENCES ubicacion ( idubicacion )
        ON DELETE NO ACTION 
        ON UPDATE NO ACTION
);

CREATE TABLE empleado (
    idempleado     CHAR(5)        NOT NULL,
    apellido       VARCHAR(50)    NOT NULL,
    nombre         VARCHAR(50)    NOT NULL,
    fecingreso     DATETIME  NOT NULL,
    email          VARCHAR(50)    NULL,
    telefono       VARCHAR(20)    NULL,
    idcargo        CHAR(3)        NOT NULL,
    iddepartamento INT            NOT NULL,
    sueldo         FLOAT          NOT NULL,
    comision       FLOAT     NULL,
    jefe           CHAR(5)        NULL,
    CONSTRAINT pk_empleado 
        PRIMARY KEY ( idempleado ),
    CONSTRAINT fk_empleado_cargo 
        FOREIGN KEY ( idcargo ) 
        REFERENCES cargo ( idcargo )
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
    CONSTRAINT fk_empleado_departamento 
        FOREIGN KEY ( iddepartamento ) 
        REFERENCES departamento ( iddepartamento )
        ON DELETE NO ACTION 
        ON UPDATE NO ACTION,
    CONSTRAINT fk_empleado_empleado 
        FOREIGN KEY ( jefe ) 
        REFERENCES empleado ( idempleado )
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

CREATE TABLE control (
    parametro   VARCHAR(20) NOT NULL,
    valor       VARCHAR(20) NOT NULL,
    CONSTRAINT pk_control PRIMARY KEY ( parametro )
);

INSERT INTO cargo ( idcargo, nombre, sueldo_min, sueldo_max ) VALUES ( 'C01', 'Gerente General', 15000, 50000 );
INSERT INTO cargo ( idcargo, nombre, sueldo_min, sueldo_max ) VALUES ( 'C02', 'Gerente', 10000, 15000 );
INSERT INTO cargo ( idcargo, nombre, sueldo_min, sueldo_max ) VALUES ( 'C03', 'Empleado', 7000, 10000 );
INSERT INTO cargo ( idcargo, nombre, sueldo_min, sueldo_max ) VALUES ( 'C04', 'Analista', 5000, 7000 );
INSERT INTO cargo ( idcargo, nombre, sueldo_min, sueldo_max ) VALUES ( 'C05', 'Vendedor', 3000, 5000 );
INSERT INTO cargo ( idcargo, nombre, sueldo_min, sueldo_max ) VALUES ( 'C06', 'Oficinista', 1500, 3000 );
INSERT INTO cargo ( idcargo, nombre, sueldo_min, sueldo_max ) VALUES ( 'C07', 'Programador', 2500, 6000 );
INSERT INTO cargo ( idcargo, nombre, sueldo_min, sueldo_max ) VALUES ( 'C08', 'Investigador', 6000, 8000 );
INSERT INTO cargo ( idcargo, nombre, sueldo_min, sueldo_max ) VALUES ( 'C09', 'Digitador', 1000, 1500 );
INSERT INTO cargo ( idcargo, nombre, sueldo_min, sueldo_max ) VALUES ( 'C10', 'Anfitriona', 1300, 1800 );

INSERT INTO ubicacion ( idubicacion, ciudad, direccion ) VALUES ( 'U01', 'Lima', 'Av. Benavides 534 - Miraflores' );
INSERT INTO ubicacion ( idubicacion, ciudad, direccion ) VALUES ( 'U02', 'Trujillo', 'Calle Primavera 1235 - Cercado' );
INSERT INTO ubicacion ( idubicacion, ciudad, direccion ) VALUES ( 'U03', 'Arequipa', 'Av. Central 2517 - Cercado' );
INSERT INTO ubicacion ( idubicacion, ciudad, direccion ) VALUES ( 'U04', 'Lima', 'Av. La Marina 3456 - San Miguel' );

INSERT INTO departamento ( iddepartamento, nombre, idubicacion ) VALUES ( 100, 'Gerencia', 'U01' );
INSERT INTO departamento ( iddepartamento, nombre, idubicacion ) VALUES ( 101, 'Contabilidad', 'U01' );
INSERT INTO departamento ( iddepartamento, nombre, idubicacion ) VALUES ( 102, 'Investigacion', 'U03' );
INSERT INTO departamento ( iddepartamento, nombre, idubicacion ) VALUES ( 103, 'Ventas', 'U01' );
INSERT INTO departamento ( iddepartamento, nombre, idubicacion ) VALUES ( 104, 'Operaciones', 'U01' );
INSERT INTO departamento ( iddepartamento, nombre, idubicacion ) VALUES ( 105, 'Sistemas', 'U04' );
INSERT INTO departamento ( iddepartamento, nombre, idubicacion ) VALUES ( 106, 'Recursos Humanos', 'U04' );
INSERT INTO departamento ( iddepartamento, nombre, idubicacion ) VALUES ( 107, 'Finanzas', 'U01' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0001', 'Coronel', 'Gustavo', '2000-04-01', 'gcoronelc@gmail.com', '996-664-457', 'C01', 100, 25000, NULL, NULL );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0002', 'Fernandez', 'Claudia', '2000-05-01', 'cfernandez@perudev.com', '9345-8365', 'C03', 100, 8000, NULL, 'E0001' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0003', 'Matsukawa', 'Sergio', '2000-04-01', 'smatsukawa@perudev.com', '9772-8369', 'C02', 102, 15000, NULL, 'E0001' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0004', 'Diaz', 'Mariela', '2000-04-10', 'mdiaz@perudev.com', '8654-6734', 'C06', 102, 1800, NULL, 'E0003' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0005', 'Martinez', 'Roberto', '2000-04-05', 'rmartinez@perudev.com', NULL, 'C08', 102, 9000, 500, 'E0003' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0006', 'Espinoza', 'Miguel', '2000-04-06', 'mespinoza@perudev.com', NULL, 'C08', 102, 7500, 500, 'E0003' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0007', 'Ramos', 'Vanessa', '2002-04-06', 'vramos@perudev.com', '9456-3456', 'C08', 102, 7000, 500, 'E0003' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0008', 'Flores', 'Julio', '2000-04-01', 'jflores@perudev.com', NULL, 'C07', 102, 3500, 1000, 'E0003' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0009', 'Marcelo', 'Ricardo', '2000-04-01', 'rmarcelo@perudev.com', '9936-2966', 'C02', 101, 15000, NULL, 'E0001' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0010', 'Barrios', 'Guisella', '2001-01-15', 'gbarrios@perudev.com', '9023-4512', 'C03', 101, 8000, NULL, 'E0009' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0011', 'Cuellar', 'Lucy', '2003-02-18', 'lcuellar@perudev.com', NULL, 'C06', 101, 2000, NULL, 'E0009' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0012', 'Valencia', 'Hugo', '2000-05-01', 'hvalencia@perudev.com', '9732-5601', 'C02', 105, 18000, NULL, 'E0001' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0013', 'Veliz', 'Fortunato', '2000-05-05', 'fveliz@perudev.com', '9826-7603', 'C04', 105, 6000, NULL, 'E0012' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0014', 'Aguero', 'Octavio', '2000-05-15', 'oaguero@perudev.com', NULL, 'C07', 105, 3000, 300, 'E0012' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0015', 'Rosales', 'Cesar', '2003-03-15', 'crosales@perudev.com', NULL, 'C07', 105, 2500, 300, 'E0012' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0016', 'Villarreal', 'Nora', '2000-05-01', 'nvillarreal@perudev.com', '9371-3641', 'C02', 103, 15000, NULL, 'E0001' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0017', 'Romero', 'Alejandra', '2000-05-03', 'aromero@perudev.com', '8345-9526', 'C03', 103, 7500, NULL, 'E0016' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0018', 'Valdiviezo', 'Jennifer', '2000-06-12', 'jvaldiviezo@perudev.com', '9263-5172', 'C06', 103, 2000, NULL, 'E0016' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0019', 'Muchotrigo', 'Omar', '2000-05-12', 'omuchotrigo@perudev.com', '9963-5542', 'C05', 103, 3500, 500, 'E0016' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0020', 'Baltazar', 'Victor', '2000-05-18', 'vbaltazar@perudev.com', '9893-4433', 'C05', 103, 3000, 800, 'E0016' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0021', 'Castillo', 'Ronald', '2001-05-18', 'rcastillo@perudev.com', '9234-3487', 'C05', 103, 3000, 800, 'E0016' );

INSERT INTO empleado ( idempleado, apellido, nombre, fecingreso, email, telefono, idcargo, iddepartamento, sueldo, comision, jefe )
VALUES ( 'E0022', 'Espilco', 'Luis', '2002-04-17', 'lespilco@perudev.com', '9554-3456', 'C05', 103, 3000, 300, 'E0016' );

INSERT INTO control ( parametro, valor ) VALUES ( 'Cargo', '10' );
INSERT INTO control ( parametro, valor ) VALUES ( 'Ubicacion', '4' );
INSERT INTO control ( parametro, valor ) VALUES ( 'Departamento', '107' );
INSERT INTO control ( parametro, valor ) VALUES ( 'Empleado', '22' );
INSERT INTO control ( parametro, valor ) VALUES ( 'Empresa', 'PeruDev' );

-- En base a la tabla EMPLOYEES, listar datos de quienes tengan un sueldo mayor a 10000.
SELECT * FROM rrhh.empleado WHERE sueldo > 10000;

/*En base a la tabla EMPLOYEES, contar cuántas personas, al aplicar un
aumento de 5%, su sueldo supere los 15000.*/
select count(rrhh.empleado.sueldo) from rrhh.empleado 
where rrhh.empleado.sueldo * 1.05 >= 15000;

-- Listar los nombres de todos los departamentos.
select nombre from rrhh.departamento;

/*Listar la cantidad de personas de la tabla EMPLOYEES, que tengan el cargo de
Programador. Y cuantas de estas personas superen el sueldo mínimo en esa
categoría.*/
select apellido, empleado.nombre, cargo.nombre, sueldo from rrhh.empleado, rrhh.cargo 
where cargo.nombre = "Programador" and sueldo >= 
(select cargo.sueldo_min from cargo where cargo.nombre = "Programador");


select nombre from rrhh.cargo where nombre = "Programador"; 
select min(sueldo) from rrhh.cargo where cargo.nombre = "Programador";









