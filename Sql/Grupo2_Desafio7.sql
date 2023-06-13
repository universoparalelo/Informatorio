SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema blog
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema blog
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `blog` ;
USE `blog` ;

-- -----------------------------------------------------
-- Table `blog`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`Usuario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NULL,
  `telefono` VARCHAR(50) NULL,
  `username` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `contraseña` VARCHAR(45) NULL,
  `estado` VARCHAR(45) NULL,
  `fecha_creacion` DATE NULL,
  `avatar` VARCHAR(45) NULL,
  `es_publico` TINYINT NULL,
  `es_colaborador` TINYINT NULL,
  `es_admin` TINYINT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blog`.`Articulo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`Articulo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_usuario` INT NOT NULL,
  `titulo` VARCHAR(45) NULL,
  `resumen` VARCHAR(45) NULL,
  `contenido` VARCHAR(45) NULL,
  `fecha_publicacion` DATE NULL,
  `estado`  TINYINT NULL,
  `imagen` VARCHAR(100) NULL,
  PRIMARY KEY (`id`),
  INDEX `id_usuario_idx` (`id_usuario` ASC) VISIBLE,
  CONSTRAINT `id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `blog`.`Usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blog`.`Comentario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`Comentario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_articulo` INT NOT NULL,
  `contenido` VARCHAR(100) NULL,
  `fecha_hora` DATETIME NULL,
  `estado` VARCHAR(45) NULL,
  `idUsuario` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_articulo_idx` (`id_articulo` ASC) VISIBLE,
  INDEX `id_usuario_idx` (`idUsuario` ASC) VISIBLE,
  CONSTRAINT `id_articulo`
    FOREIGN KEY (`id_articulo`)
    REFERENCES `blog`.`Articulo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idUsuario`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `blog`.`Usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blog`.`Categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`Categoria` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_categoria` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  `imagen` VARCHAR(100) NULL,
  `estado` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `id_categoria_idx` (`id_categoria` ASC) VISIBLE,
  CONSTRAINT `id_categoria`
    FOREIGN KEY (`id_categoria`)
    REFERENCES `blog`.`Categoria` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blog`.`categoria_articulo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`categoria_articulo` (
  `idArticulo` INT NOT NULL,
  `idCategoria` INT NOT NULL,
  INDEX `id_categoria_idx` (`idCategoria` ASC) VISIBLE,
  INDEX `id_articulo_idx` (`idArticulo` ASC) VISIBLE,
  CONSTRAINT `idCategoria`
    FOREIGN KEY (`idCategoria`)
    REFERENCES `blog`.`Categoria` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idArticulo`
    FOREIGN KEY (`idArticulo`)
    REFERENCES `blog`.`Articulo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



/*CONSIGNAS*/


/* Esta instrucción agrega un usuario administrador y colaboradores y público a la tabla usuario.
   Hay un usuario con rol de admin, cuatro con rol de colaborador y cinco con rol de público, cuyos campos
   es_publico, es_colaborador y es_admin son booleanos. */

INSERT INTO `blog`.`usuario` (`nombre`, `apellido`, `telefono`, `username`, `email`, `contraseña`, `estado`, `fecha_creacion`, `avatar`, `es_publico`, `es_colaborador`, `es_admin`) VALUES ('Luis', 'Fernandez', '3624763456', 'luismiguel', 'luismiguel@gmail.com', 'prueba123', 'activo', '2023-06-09', 'prueba1', '0', '0', '1');
INSERT INTO `blog`.`usuario` (`nombre`, `apellido`, `telefono`, `username`, `email`, `contraseña`, `estado`, `fecha_creacion`, `avatar`, `es_publico`, `es_colaborador`, `es_admin`) VALUES ('Fernando', 'Arriola', '3467234578', 'ferarriola23', 'ferarriola@gmail.com', 'prueba456', 'activo', '2023-06-09', 'prueba2', '0', '1 ', '0');
INSERT INTO `blog`.`usuario` (`nombre`, `apellido`, `telefono`, `username`, `email`, `contraseña`, `estado`, `fecha_creacion`, `avatar`, `es_publico`, `es_colaborador`, `es_admin`) VALUES ('Mauro', 'Icardi', '3467985674', 'Mauicardi', 'mauroicardi@gmail.com', 'prueba234', 'activo', '2023-06-09', 'prueba3', '0 ', '1', '0');
INSERT INTO `blog`.`usuario` (`nombre`, `apellido`, `telefono`, `username`, `email`, `contraseña`, `estado`, `fecha_creacion`, `avatar`, `es_publico`, `es_colaborador`, `es_admin`) VALUES ('Agostina', 'Ruiz', '3456123456', 'agostinaruiz@gmai.com', 'agosruiz@gmail.com', 'prueba789', 'activo', '2023-06-09', 'prueba4', '0', '1', '0');
INSERT INTO `blog`.`usuario` (`nombre`, `apellido`, `telefono`, `username`, `email`, `contraseña`, `estado`, `fecha_creacion`, `avatar`, `es_publico`, `es_colaborador`, `es_admin`) VALUES ('Miguel', 'Rodriguez', '3456987623', 'migueruiz', 'miguelrodriguez@gmail.com', 'pruena843', 'activo', '2023-06-09', 'prueba5', '0', '1', '0');
INSERT INTO `blog`.`usuario` (`nombre`, `apellido`, `telefono`, `username`, `email`, `contraseña`, `estado`, `fecha_creacion`, `avatar`, `es_publico`, `es_colaborador`, `es_admin`) VALUES ('Mario', 'Filiberti', '3456789657', 'marito23', 'mariofiliberti@gmail.com', 'prueba814', 'activo', '2023-06-09', 'prueba6', '1', '0', '0');
INSERT INTO `blog`.`usuario` (`nombre`, `apellido`, `telefono`, `username`, `email`, `contraseña`, `estado`, `fecha_creacion`, `avatar`, `es_publico`, `es_colaborador`, `es_admin`) VALUES ('Ernesto', 'Bonavena', '35672344556', 'ernesto34', 'ernestobona@gmail.com', 'prueba543', 'activo', '2023-06-09', 'prueba7', '1', '0', '0');
INSERT INTO `blog`.`usuario` (`nombre`, `apellido`, `telefono`, `username`, `email`, `contraseña`, `estado`, `fecha_creacion`, `avatar`, `es_publico`, `es_colaborador`, `es_admin`) VALUES ('Catalina', 'Suarez', '3624854321', 'cata98', 'catasuarez@gmail.com', 'prueba923', 'activo', '2023-06-09', 'prueba8', '1', '0', '0');
INSERT INTO `blog`.`usuario` (`nombre`, `apellido`, `telefono`, `username`, `email`, `contraseña`, `estado`, `fecha_creacion`, `avatar`, `es_publico`, `es_colaborador`, `es_admin`) VALUES ('Juan', 'Riquelme', '3625139875', 'Juan21', 'juanriquelme@gmail.com', 'prueba3221', 'activo', '2023-06-09', 'prueba9', '1', '0', '0');
INSERT INTO `blog`.`usuario` (`nombre`, `apellido`, `telefono`, `username`, `email`, `contraseña`, `estado`, `fecha_creacion`, `avatar`, `es_publico`, `es_colaborador`, `es_admin`) VALUES ('Patricia', 'Gimenez', '3623982314', 'patri112', 'patriciagimenez@gmail.com', 'prueba2159', 'activo', '2023-06-09', 'prueba10', '1', '0', '0');




/*Agregar el comando necesario para actualizar el rol a admin de uno de los usuarios
agregado con rol de colaborador.*/

update usuario set es_admin = 1, es_colaborador = 0 where es_colaborador = 1 limit 1;


/*Agregar el comando necesario que introduzca en la tabla articulo, 3 artículos con
estado TRUE y uno con estado FALSE. Donde el campo estado en todas las tablas es
Booleano.*/

INSERT INTO `blog`.`articulo` (`id_usuario`, `titulo`, `resumen`, `contenido`, `fecha_publicacion`, `estado`, `imagen`) VALUES ('1', 'articulo1', 'resumen articulo1', 'contenido articulo 1', '2023-06-09', '1', 'imagen1');
INSERT INTO `blog`.`articulo` (`id_usuario`, `titulo`, `resumen`, `contenido`, `fecha_publicacion`, `estado`, `imagen`) VALUES ('2', 'articulo2', 'resumen articulo 2', 'contenido articulo 2', '2023-06-09', '1', 'imagen2');
INSERT INTO `blog`.`articulo` (`id_usuario`, `titulo`, `resumen`, `contenido`, `fecha_publicacion`, `estado`, `imagen`) VALUES ('3', 'articulo3', 'resumen articulo 3', 'contenido articulo 3', '2023-09-06', '1', 'imagen3');
INSERT INTO `blog`.`articulo` (`id_usuario`, `titulo`, `resumen`, `contenido`, `fecha_publicacion`, `estado`, `imagen`) VALUES ('4', 'articulo4', 'resumen articulo 4', 'contenido articulo 4', '2023-09-06', '0', 'imagen4');




/*Agregar el comando necesario para eliminar el artículo que tenga estado FALSE.*/

DELETE FROM articulo WHERE id = (SELECT id FROM (SELECT * FROM articulo WHERE estado = 0) AS subquery);


/*Agregar el comando necesario que introduzca 3 comentarios al primer artículo
agregado y 2 comentarios al segundo artículo
*/

INSERT INTO `blog`.`comentario` (`id_articulo`, `contenido`, `fecha_hora`, `idUsuario`) VALUES ('1', 'comentario 1', '2023-06-09 14:34:25', '1');
INSERT INTO `blog`.`comentario` (`id_articulo`, `contenido`, `fecha_hora`, `idUsuario`) VALUES ('1', 'comentario 2', '2023-06-09 14:34:25', '2');
INSERT INTO `blog`.`comentario` (`id_articulo`, `contenido`, `fecha_hora`, `idUsuario`) VALUES ('1', 'comentario 3', '2023-06-09 14:34:25', '3');
INSERT INTO `blog`.`comentario` (`id_articulo`, `contenido`, `fecha_hora`, `idUsuario`) VALUES ('2', 'comentario 4', '2023-06-09 14:34:25', '4');
INSERT INTO `blog`.`comentario` (`id_articulo`, `contenido`, `fecha_hora`, `idUsuario`) VALUES ('2', 'comentario 5', '2023-06-09 14:34:25', '5');



/*Agregar el comando necesario para listar todos los artículos que tengan
comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el
nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho
comentario, agrupados por artículos.*/
 

SELECT articulo.titulo, articulo.fecha_publicacion, usuario.nombre, comentario.fecha_hora
FROM blog.articulo
JOIN blog.comentario ON articulo.id = comentario.id_articulo
JOIN blog.usuario ON comentario.IdUsuario = usuario.id
GROUP BY articulo.titulo, articulo.fecha_publicacion, usuario.nombre, comentario.fecha_hora;
